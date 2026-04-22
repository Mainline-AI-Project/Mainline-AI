# # from rest_framework.decorators import api_view
# # from rest_framework.response import Response
# # from .models import User, Chat, Message
# # from .jwt import create_jwt
# # from django.views.decorators.csrf import csrf_exempt
# # import uuid

# # @csrf_exempt
# # @api_view(["POST"])
# # def signup_user(request):
# #     data = request.data

# #     # --- REQUIRED FIELDS ---
# #     username = data.get("username")
# #     email = data.get("email")
# #     password = data.get("password")
# #     name = data.get("name", "")
# #     plan = data.get("plan")  # optional, frontend sends selected plan

# #     if not email or not password:
# #         return Response({"message": "Email and password required"}, status=400)

# #     # --- CHECK DUPLICATES ---
# #     if User.objects(username=username).first():
# #         return Response({"message": "Username already taken"}, status=400)
# #     if User.objects(email=email).first():
# #         return Response({"message": "Email already used"}, status=400)

# #     # --- CREATE USER ---
# #     user = User(
# #         username=username or email.split("@")[0],  # fallback if username not provided
# #         email=email,
# #         name=name,
# #     )
# #     if plan:
# #         user.plan = plan  # Optional: make sure you add `plan` field in model if you want to store
# #     user.set_password(password)
# #     user.save()

# #     # --- CREATE JWT TOKEN ---
# #     token = create_jwt(user)

# #     return Response({
# #         "token": token,
# #         "user": {
# #             "username": user.username,
# #             "email": user.email,
# #             "name": user.name,
# #             "plan": getattr(user, "plan", None)
# #         }
# #     }, status=201)

# # @csrf_exempt
# # @api_view(['POST'])
# # def pin_chat(request, username, chat_id):
# #     user = User.objects(username=username).first()
# #     if not user:
# #         return Response({"message": "User not found"}, status=404)
# #     pinned_value = request.data.get('pinned', True)
# #     # Find chat
# #     chat = next((c for c in user.chats if c.chat_id == chat_id), None)
# #     if not chat:
# #         return Response({"message": "Chat not found"}, status=404)
# #     # Set pinned
# #     chat.pinned = pinned_value
# #     # Mark user as changed so MongoEngine saves embedded document properly
# #     user.save()
# #     return Response({'status': 'ok', 'chat_id': chat_id, 'pinned': pinned_value})


# # @csrf_exempt
# # @api_view(["POST"])
# # def login_user(request):
# #     data = request.data

# #     if not data.get("username") or not data.get("password"):
# #         return Response({"message": "Username and password required"}, status=400)

# #     user = User.objects(username=data["username"]).first()
# #     if not user or not user.check_password(data["password"]):
# #         return Response({"message": "Invalid credentials"}, status=401)

# #     token = create_jwt(user)
# #     return Response({
# #         "token": token,
# #         "user": {"username": user.username, "name": user.name}
# #     })

# # @csrf_exempt
# # @api_view(["GET"])
# # def get_chats(request, username):
# #     user = User.objects(username=username).first()
# #     if not user:
# #         return Response({"message": "User not found"}, status=404)

# #     chats_data = [
# #         {
# #             "chat_id": chat.chat_id,
# #             "title": chat.title,
# #             "pinned": getattr(chat, "pinned", False),  # include pinned
# #             "messages": [{"text": m.text, "sender": m.sender} for m in chat.messages]
# #         }
# #         for chat in user.chats
# #     ]
# #     return Response({"chats": chats_data})


# # # Start new chat
# # @csrf_exempt
# # @api_view(["POST"])
# # def start_new_chat(request, username):
# #     user = User.objects(username=username).first()
# #     if not user:
# #         return Response({"message": "User not found"}, status=404)

# #     chat_id = str(uuid.uuid4())
# #     chat_title = request.data.get("title", f"Chat {len(user.chats)+1}")
# #     new_chat = Chat(chat_id=chat_id, title=chat_title, pinned=False)
# #     user.chats.append(new_chat)
# #     user.save()

# #     return Response({"chat_id": chat_id, "title": chat_title})

# # # Add message to a chat
# # @csrf_exempt
# # @api_view(["POST"])
# # def add_message(request, username, chat_id):
# #     user = User.objects(username=username).first()
# #     if not user:
# #         return Response({"message": "User not found"}, status=404)

# #     chat = next((c for c in user.chats if c.chat_id == chat_id), None)
# #     if not chat:
# #         return Response({"message": "Chat not found"}, status=404)

# #     text = request.data.get("text")
# #     sender = request.data.get("sender", "user")

# #     chat.messages.append(Message(text=text, sender=sender))
# #     user.save()

# #     return Response({"message": "Message added"})

# # # Delete a chat
# # @csrf_exempt
# # @api_view(["DELETE"])
# # def delete_chat(request, username, chat_id):
# #     user = User.objects(username=username).first()
# #     if not user:
# #         return Response({"message": "User not found"}, status=404)

# #     chat = next((c for c in user.chats if c.chat_id == chat_id), None)
# #     if not chat:
# #         return Response({"message": "Chat not found"}, status=404)

# #     user.chats = [c for c in user.chats if c.chat_id != chat_id]
# #     user.save()
# #     return Response({"message": "Chat deleted"})


# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from django.views.decorators.csrf import csrf_exempt
# from mongoengine.queryset.visitor import Q
# import uuid

# from .models import User, Chat, Message
# from .jwt import create_jwt

# from django.http import JsonResponse
# import json
# from .rag import query_rag

# from django.http import JsonResponse
# from django.views.decorators.http import require_POST
# from django.core.mail import send_mail
# from django.conf import settings


# @csrf_exempt
# @api_view(["POST"])
# def signup_user(request):
#     data = request.data

#     email = data.get("email", "").strip().lower()
#     password = data.get("password")
#     username = data.get("username")
#     name = data.get("name", "")
#     plan = data.get("plan")

#     if not email or not password:
#         return Response(
#             {"message": "Email and password required"},
#             status=400
#         )

#     # ---- CHECK EMAIL ----
#     if User.objects(email=email).first():
#         return Response(
#             {"message": "An account already exists for this email"},
#             status=400
#         )

#     # ---- CHECK USERNAME ----
#     if username:
#         if User.objects(username=username).first():
#             return Response(
#                 {"message": "Username already taken"},
#                 status=400
#             )
#     else:
#         # fallback username from email
#         base_username = email.split("@")[0]
#         username = base_username
#         counter = 1
#         while User.objects(username=username).first():
#             username = f"{base_username}{counter}"
#             counter += 1

#     # ---- CREATE USER ----
#     user = User(
#         username=username,
#         email=email,
#         name=name,
#         plan=plan
#     )
#     user.set_password(password)
#     user.save()

#     token = create_jwt(user)

#     return Response({
#         "token": token,
#         "user": {
#             "username": user.username,
#             "email": user.email,
#             "name": user.name,
#             "plan": user.plan
#         }
#     }, status=201)

# @csrf_exempt
# @api_view(["POST"])
# def login_user(request):
#     data = request.data

#     identifier = data.get("identifier", "").strip().lower()
#     password = data.get("password")

#     if not identifier or not password:
#         return Response(
#             {"message": "Username/email and password required"},
#             status=400
#         )

#     user = User.objects(
#         Q(username=identifier) | Q(email=identifier)
#     ).first()

#     if not user or not user.check_password(password):
#         return Response(
#             {"message": "Invalid credentials"},
#             status=401
#         )

#     token = create_jwt(user)

#     return Response({
#         "token": token,
#         "user": {
#             "username": user.username,
#             "email": user.email,
#             "name": user.name,
#             "plan": user.plan
#         }
#     }, status=200)

# @csrf_exempt
# @api_view(["POST"])
# def pin_chat(request, username, chat_id):
#     user = User.objects(username=username).first()
#     if not user:
#         return Response({"message": "User not found"}, status=404)

#     chat = next((c for c in user.chats if c.chat_id == chat_id), None)
#     if not chat:
#         return Response({"message": "Chat not found"}, status=404)

#     chat.pinned = bool(request.data.get("pinned", True))
#     user.save()

#     return Response({
#         "status": "ok",
#         "chat_id": chat_id,
#         "pinned": chat.pinned
#     })

# @csrf_exempt
# @api_view(["GET"])
# def get_chats(request, username):
#     user = User.objects(username=username).first()
#     if not user:
#         return Response({"message": "User not found"}, status=404)

#     chats_data = [
#         {
#             "chat_id": chat.chat_id,
#             "title": chat.title,
#             "pinned": chat.pinned,
#             "messages": [
#                 {"text": m.text, "sender": m.sender}
#                 for m in chat.messages
#             ]
#         }
#         for chat in user.chats
#     ]

#     return Response({"chats": chats_data})

# @csrf_exempt
# @api_view(["POST"])
# def start_new_chat(request, username):
#     user = User.objects(username=username).first()
#     if not user:
#         return Response({"message": "User not found"}, status=404)

#     chat_id = str(uuid.uuid4())
#     title = request.data.get("title", f"Chat {len(user.chats) + 1}")

#     user.chats.append(Chat(
#         chat_id=chat_id,
#         title=title,
#         pinned=False
#     ))
#     user.save()

#     return Response({
#         "chat_id": chat_id,
#         "title": title
#     })

# @csrf_exempt
# @api_view(["POST"])
# def add_message(request, username, chat_id):
#     user = User.objects(username=username).first()
#     if not user:
#         return Response({"message": "User not found"}, status=404)

#     chat = next((c for c in user.chats if c.chat_id == chat_id), None)
#     if not chat:
#         return Response({"message": "Chat not found"}, status=404)

#     text = request.data.get("text")
#     sender = request.data.get("sender", "user")

#     chat.messages.append(Message(text=text, sender=sender))
#     user.save()

#     return Response({"message": "Message added"})

# @csrf_exempt
# @api_view(["DELETE"])
# def delete_chat(request, username, chat_id):
#     user = User.objects(username=username).first()
#     if not user:
#         return Response({"message": "User not found"}, status=404)

#     user.chats = [c for c in user.chats if c.chat_id != chat_id]
#     user.save()

#     return Response({"message": "Chat deleted"})



# @csrf_exempt
# def rag_query(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         user_text = data.get("text", "")
#         response_text = query_rag(user_text)
#         return JsonResponse({"response": response_text})
#     return JsonResponse({"error": "POST only"}, status=400)

# @csrf_exempt
# @require_POST
# def forgot_password(request):
#     """Receive email, send reset link if user exists."""
#     try:
#         data = json.loads(request.body)
#         email = data.get("email", "").strip().lower()
#     except (json.JSONDecodeError, AttributeError):
#         return JsonResponse({"error": "Invalid request body."}, status=400)

#     if not email:
#         return JsonResponse({"error": "Email is required."}, status=400)

#     # Always return 200 to avoid leaking whether an email is registered
#     try:
#         user = User.objects.get(email=email)
#         token = user.generate_reset_token()

#         reset_url = f"{settings.FRONTEND_URL}/reset-password?token={token}"

#         send_mail(
#             subject="Reset your Mainline-AI password",
#             message=(
#                 f"Hi {user.name or user.username},\n\n"
#                 f"Click the link below to reset your password. "
#                 f"It expires in 1 hour.\n\n{reset_url}\n\n"
#                 f"If you didn't request this, you can ignore this email."
#             ),
#             from_email=settings.DEFAULT_FROM_EMAIL,
#             recipient_list=[user.email],
#             fail_silently=False,
#         )
#     except User.DoesNotExist:
#         pass  # Don't reveal that email doesn't exist

#     return JsonResponse({
#         "message": "If that email is registered, a reset link has been sent."
#     })


# @csrf_exempt
# @require_POST
# def reset_password(request):
#     """Validate token and update the user's password."""
#     try:
#         data = json.loads(request.body)
#         token = data.get("token", "").strip()
#         new_password = data.get("password", "")
#     except (json.JSONDecodeError, AttributeError):
#         return JsonResponse({"error": "Invalid request body."}, status=400)

#     if not token or not new_password:
#         return JsonResponse({"error": "Token and password are required."}, status=400)

#     if len(new_password) < 8:
#         return JsonResponse({"error": "Password must be at least 8 characters."}, status=400)

#     try:
#         user = User.objects.get(reset_token=token)
#     except User.DoesNotExist:
#         return JsonResponse({"error": "Invalid or expired reset link."}, status=400)

#     if not user.is_reset_token_valid(token):
#         return JsonResponse({"error": "This reset link has expired."}, status=400)

#     user.set_password(new_password)
#     user.clear_reset_token()

#     return JsonResponse({"message": "Password updated successfully."})


# #Test debug
# import traceback

# def signup(request):
#     try:
#         # ... your existing signup logic
#         pass
#     except Exception as e:
#         traceback.print_exc()  # prints full stack trace in terminal
#         return JsonResponse({"error": str(e)}, status=500)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from mongoengine.queryset.visitor import Q
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core.mail import send_mail
from django.conf import settings
import uuid
import json
import traceback

from .models import User, Chat, Message
from .jwt_utils import create_jwt, token_generator
from .rag import query_rag
import logging


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

        if User.objects(email=email).first():
            return Response({"message": "An account already exists for this email"}, status=400)

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

        user = User(username=username, email=email, name=name, plan=plan)
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

        user = User.objects(Q(username=identifier) | Q(email=identifier)).first()

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
    return Response({"status": "ok", "chat_id": chat_id, "pinned": chat.pinned})


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

    chat.messages.append(Message(text=request.data.get("text"), sender=request.data.get("sender", "user")))
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


@csrf_exempt
def rag_query(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_text = data.get("text", "")
        response_text = query_rag(user_text)
        return JsonResponse({"response": response_text})
    return JsonResponse({"error": "POST only"}, status=400)

@csrf_exempt
def forgot_password(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid method"}, status=405)

    data = json.loads(request.body)
    email = data.get("email")

    if not email:
        return JsonResponse({"error": "Email required"}, status=400)

    user = User.objects(email=email).first()  # 👈 MongoEngine query

    # Always return same response (security best practice)
    if not user:
        return JsonResponse({"message": "If email exists, reset link sent"})

    token = user.generate_reset_token()

    uid = str(user.id)

    reset_link = f"{settings.FRONTEND_URL}/reset-password/{uid}/{token}"

    send_mail(
        subject="Password Reset Request",
        message=f"Click here to reset your password:\n{reset_link}",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email],
        fail_silently=False,
    )

    return JsonResponse({"message": "Email sent"})

@csrf_exempt
def reset_password(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid method"}, status=405)

    data = json.loads(request.body)

    uid = data.get("uid")
    token = data.get("token")
    password = data.get("password")

    if not all([uid, token, password]):
        return JsonResponse({"error": "Missing fields"}, status=400)

    try:
        user = User.objects(id=uid).first()  # MongoEngine lookup

        if not user:
            return JsonResponse({"error": "Invalid user"}, status=400)

        if not user.is_reset_token_valid(token):
            return JsonResponse({"error": "Invalid or expired token"}, status=400)

        user.set_password(password)
        user.clear_reset_token()
        user.save()

        return JsonResponse({"message": "Password reset successful"})

    except Exception as e:
        return JsonResponse({"error": "Invalid request"}, status=400)
