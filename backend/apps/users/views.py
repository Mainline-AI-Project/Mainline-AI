from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core.mail import send_mail
from django.conf import settings
from mongoengine.queryset.visitor import Q

import uuid
import json
import traceback
import logging

from .models import User, Chat, Message
from .jwt_utils import create_jwt
from .rag import query_rag

logger = logging.getLogger(__name__)

# =========================
# AUTH
# =========================

@csrf_exempt
@api_view(["POST"])
def signup_user(request):
    try:
        data = request.data

        email = data.get("email", "").strip().lower()
        password = data.get("password")
        username = data.get("username")
        name = data.get("name", "")
        plan = data.get("plan")

        if not email or not password:
            return Response({"message": "Email and password required"}, status=400)

        # Check email
        if User.objects(email=email).first():
            return Response({"message": "Email already in use"}, status=400)

        # Handle username
        if username:
            if User.objects(username=username).first():
                return Response({"message": "Username already taken"}, status=400)
        else:
            base_username = email.split("@")[0]
            username = base_username
            counter = 1
            while User.objects(username=username).first():
                username = f"{base_username}{counter}"
                counter += 1

        # Create user
        user = User(
            username=username,
            email=email,
            name=name,
            plan=plan
        )
        user.set_password(password)
        user.save()

        token = create_jwt(user)

        return Response({
            "token": token,
            "user": {
                "username": user.username,
                "email": user.email,
                "name": user.name,
                "plan": user.plan
            }
        }, status=201)

    except Exception as e:
        traceback.print_exc()
        return Response({"message": f"Signup failed: {str(e)}"}, status=500)


@csrf_exempt
@api_view(["POST"])
def login_user(request):
    try:
        data = request.data

        identifier = data.get("identifier", "").strip().lower()
        password = data.get("password")

        if not identifier or not password:
            return Response({"message": "Username/email and password required"}, status=400)

        user = User.objects(
            Q(username=identifier) | Q(email=identifier)
        ).first()

        if not user or not user.check_password(password):
            return Response({"message": "Invalid credentials"}, status=401)

        token = create_jwt(user)

        return Response({
            "token": token,
            "user": {
                "username": user.username,
                "email": user.email,
                "name": user.name,
                "plan": user.plan
            }
        }, status=200)

    except Exception as e:
        traceback.print_exc()
        return Response({"message": f"Login failed: {str(e)}"}, status=500)


# =========================
# CHAT
# =========================

@csrf_exempt
@api_view(["POST"])
def pin_chat(request, username, chat_id):
    user = User.objects(username=username).first()
    if not user:
        return Response({"message": "User not found"}, status=404)

    chat = next((c for c in user.chats if c.chat_id == chat_id), None)
    if not chat:
        return Response({"message": "Chat not found"}, status=404)

    chat.pinned = bool(request.data.get("pinned", True))
    user.save()

    return Response({
        "status": "ok",
        "chat_id": chat_id,
        "pinned": chat.pinned
    })


@csrf_exempt
@api_view(["GET"])
def get_chats(request, username):
    user = User.objects(username=username).first()
    if not user:
        return Response({"message": "User not found"}, status=404)

    chats_data = [
        {
            "chat_id": chat.chat_id,
            "title": chat.title,
            "pinned": chat.pinned,
            "messages": [{"text": m.text, "sender": m.sender} for m in chat.messages]
        }
        for chat in user.chats
    ]

    return Response({"chats": chats_data})


@csrf_exempt
@api_view(["POST"])
def start_new_chat(request, username):
    user = User.objects(username=username).first()
    if not user:
        return Response({"message": "User not found"}, status=404)

    chat_id = str(uuid.uuid4())
    title = request.data.get("title", f"Chat {len(user.chats) + 1}")

    user.chats.append(Chat(chat_id=chat_id, title=title, pinned=False))
    user.save()

    return Response({"chat_id": chat_id, "title": title})


@csrf_exempt
@api_view(["POST"])
def add_message(request, username, chat_id):
    user = User.objects(username=username).first()
    if not user:
        return Response({"message": "User not found"}, status=404)

    chat = next((c for c in user.chats if c.chat_id == chat_id), None)
    if not chat:
        return Response({"message": "Chat not found"}, status=404)

    chat.messages.append(
        Message(
            text=request.data.get("text"),
            sender=request.data.get("sender", "user")
        )
    )
    user.save()

    return Response({"message": "Message added"})


@csrf_exempt
@api_view(["DELETE"])
def delete_chat(request, username, chat_id):
    user = User.objects(username=username).first()
    if not user:
        return Response({"message": "User not found"}, status=404)

    user.chats = [c for c in user.chats if c.chat_id != chat_id]
    user.save()

    return Response({"message": "Chat deleted"})


# =========================
# RAG
# =========================

@csrf_exempt
def rag_query(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_text = data.get("text", "")
        response_text = query_rag(user_text)
        return JsonResponse({"response": response_text})

    return JsonResponse({"error": "POST only"}, status=400)


# =========================
# PASSWORD RESET
# =========================

@csrf_exempt
@require_POST
def forgot_password(request):
    try:
        data = json.loads(request.body)
        email = data.get("email", "").strip().lower()
    except:
        return JsonResponse({"error": "Invalid request body"}, status=400)

    if not email:
        return JsonResponse({"error": "Email is required"}, status=400)

    try:
        user = User.objects(email=email).first()

        if user:
            token = user.generate_reset_token()
            reset_url = f"{settings.FRONTEND_URL}/reset-password?token={token}"

            send_mail(
                subject="Reset your password",
                message=f"Reset your password:\n{reset_url}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                fail_silently=False,
            )

            logger.info(f"Reset email sent to {user.email}")

    except Exception as e:
        logger.error(f"EMAIL ERROR: {str(e)}")
        return JsonResponse({"error": "Email failed"}, status=500)

    return JsonResponse({
        "message": "If that email exists, a reset link was sent"
    })


@csrf_exempt
@require_POST
def reset_password(request):
    try:
        data = json.loads(request.body)
        token = data.get("token")
        new_password = data.get("password")
    except:
        return JsonResponse({"error": "Invalid request"}, status=400)

    if not token or not new_password:
        return JsonResponse({"error": "Missing fields"}, status=400)

    if len(new_password) < 8:
        return JsonResponse({"error": "Password too short"}, status=400)

    user = User.objects(reset_token=token).first()

    if not user:
        return JsonResponse({"error": "Invalid token"}, status=400)

    if not user.is_reset_token_valid(token):
        return JsonResponse({"error": "Token expired"}, status=400)

    user.set_password(new_password)
    user.clear_reset_token()

    return JsonResponse({"message": "Password reset successful"})
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core.mail import send_mail
from django.conf import settings
from mongoengine.queryset.visitor import Q

import uuid
import json
import traceback
import logging

from .models import User, Chat, Message
from .jwt_utils import create_jwt
from .rag import query_rag

logger = logging.getLogger(__name__)

# =========================
# AUTH
# =========================

@csrf_exempt
@api_view(["POST"])
def signup_user(request):
    try:
        data = request.data

        email = data.get("email", "").strip().lower()
        password = data.get("password")
        username = data.get("username")
        name = data.get("name", "")
        plan = data.get("plan")

        if not email or not password:
            return Response({"message": "Email and password required"}, status=400)

        # Check email
        if User.objects(email=email).first():
            return Response({"message": "Email already in use"}, status=400)

        # Handle username
        if username:
            if User.objects(username=username).first():
                return Response({"message": "Username already taken"}, status=400)
        else:
            base_username = email.split("@")[0]
            username = base_username
            counter = 1
            while User.objects(username=username).first():
                username = f"{base_username}{counter}"
                counter += 1

        # Create user
        user = User(
            username=username,
            email=email,
            name=name,
            plan=plan
        )
        user.set_password(password)
        user.save()

        token = create_jwt(user)

        return Response({
            "token": token,
            "user": {
                "username": user.username,
                "email": user.email,
                "name": user.name,
                "plan": user.plan
            }
        }, status=201)

    except Exception as e:
        traceback.print_exc()
        return Response({"message": f"Signup failed: {str(e)}"}, status=500)


@csrf_exempt
@api_view(["POST"])
def login_user(request):
    try:
        data = request.data

        identifier = data.get("identifier", "").strip().lower()
        password = data.get("password")

        if not identifier or not password:
            return Response({"message": "Username/email and password required"}, status=400)

        user = User.objects(
            Q(username=identifier) | Q(email=identifier)
        ).first()

        if not user or not user.check_password(password):
            return Response({"message": "Invalid credentials"}, status=401)

        token = create_jwt(user)

        return Response({
            "token": token,
            "user": {
                "username": user.username,
                "email": user.email,
                "name": user.name,
                "plan": user.plan
            }
        }, status=200)

    except Exception as e:
        traceback.print_exc()
        return Response({"message": f"Login failed: {str(e)}"}, status=500)


# =========================
# CHAT
# =========================

@csrf_exempt
@api_view(["POST"])
def pin_chat(request, username, chat_id):
    user = User.objects(username=username).first()
    if not user:
        return Response({"message": "User not found"}, status=404)

    chat = next((c for c in user.chats if c.chat_id == chat_id), None)
    if not chat:
        return Response({"message": "Chat not found"}, status=404)

    chat.pinned = bool(request.data.get("pinned", True))
    user.save()

    return Response({
        "status": "ok",
        "chat_id": chat_id,
        "pinned": chat.pinned
    })


@csrf_exempt
@api_view(["GET"])
def get_chats(request, username):
    user = User.objects(username=username).first()
    if not user:
        return Response({"message": "User not found"}, status=404)

    chats_data = [
        {
            "chat_id": chat.chat_id,
            "title": chat.title,
            "pinned": chat.pinned,
            "messages": [{"text": m.text, "sender": m.sender} for m in chat.messages]
        }
        for chat in user.chats
    ]

    return Response({"chats": chats_data})


@csrf_exempt
@api_view(["POST"])
def start_new_chat(request, username):
    user = User.objects(username=username).first()
    if not user:
        return Response({"message": "User not found"}, status=404)

    chat_id = str(uuid.uuid4())
    title = request.data.get("title", f"Chat {len(user.chats) + 1}")

    user.chats.append(Chat(chat_id=chat_id, title=title, pinned=False))
    user.save()

    return Response({"chat_id": chat_id, "title": title})


@csrf_exempt
@api_view(["POST"])
def add_message(request, username, chat_id):
    user = User.objects(username=username).first()
    if not user:
        return Response({"message": "User not found"}, status=404)

    chat = next((c for c in user.chats if c.chat_id == chat_id), None)
    if not chat:
        return Response({"message": "Chat not found"}, status=404)

    chat.messages.append(
        Message(
            text=request.data.get("text"),
            sender=request.data.get("sender", "user")
        )
    )
    user.save()

    return Response({"message": "Message added"})


@csrf_exempt
@api_view(["DELETE"])
def delete_chat(request, username, chat_id):
    user = User.objects(username=username).first()
    if not user:
        return Response({"message": "User not found"}, status=404)

    user.chats = [c for c in user.chats if c.chat_id != chat_id]
    user.save()

    return Response({"message": "Chat deleted"})


# =========================
# RAG
# =========================

@csrf_exempt
def rag_query(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_text = data.get("text", "")
        response_text = query_rag(user_text)
        return JsonResponse({"response": response_text})

    return JsonResponse({"error": "POST only"}, status=400)


# =========================
# PASSWORD RESET
# =========================

@csrf_exempt
@require_POST
def forgot_password(request):
    try:
        data = json.loads(request.body)
        email = data.get("email", "").strip().lower()
    except:
        return JsonResponse({"error": "Invalid request body"}, status=400)

    if not email:
        return JsonResponse({"error": "Email is required"}, status=400)

    try:
        user = User.objects(email=email).first()

        if user:
            token = user.generate_reset_token()
            reset_url = f"{settings.FRONTEND_URL}/reset-password?token={token}"

            send_mail(
                subject="Reset your password",
                message=f"Reset your password:\n{reset_url}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                fail_silently=False,
            )

            logger.info(f"Reset email sent to {user.email}")

    except Exception as e:
        logger.error(f"EMAIL ERROR: {str(e)}")
        return JsonResponse({"error": "Email failed"}, status=500)

    return JsonResponse({
        "message": "If that email exists, a reset link was sent"
    })


@csrf_exempt
@require_POST
def reset_password(request):
    try:
        data = json.loads(request.body)
        token = data.get("token")
        new_password = data.get("password")
    except:
        return JsonResponse({"error": "Invalid request"}, status=400)

    if not token or not new_password:
        return JsonResponse({"error": "Missing fields"}, status=400)

    if len(new_password) < 8:
        return JsonResponse({"error": "Password too short"}, status=400)

    user = User.objects(reset_token=token).first()

    if not user:
        return JsonResponse({"error": "Invalid token"}, status=400)

    if not user.is_reset_token_valid(token):
        return JsonResponse({"error": "Token expired"}, status=400)

    user.set_password(new_password)
    user.clear_reset_token()

    return JsonResponse({"message": "Password reset successful"})
