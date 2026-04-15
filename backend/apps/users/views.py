# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import User, Chat, Message
# from .jwt import create_jwt
# from django.views.decorators.csrf import csrf_exempt
# import uuid

# @csrf_exempt
# @api_view(["POST"])
# def signup_user(request):
#     data = request.data

#     # --- REQUIRED FIELDS ---
#     username = data.get("username")
#     email = data.get("email")
#     password = data.get("password")
#     name = data.get("name", "")
#     plan = data.get("plan")  # optional, frontend sends selected plan

#     if not email or not password:
#         return Response({"message": "Email and password required"}, status=400)

#     # --- CHECK DUPLICATES ---
#     if User.objects(username=username).first():
#         return Response({"message": "Username already taken"}, status=400)
#     if User.objects(email=email).first():
#         return Response({"message": "Email already used"}, status=400)

#     # --- CREATE USER ---
#     user = User(
#         username=username or email.split("@")[0],  # fallback if username not provided
#         email=email,
#         name=name,
#     )
#     if plan:
#         user.plan = plan  # Optional: make sure you add `plan` field in model if you want to store
#     user.set_password(password)
#     user.save()

#     # --- CREATE JWT TOKEN ---
#     token = create_jwt(user)

#     return Response({
#         "token": token,
#         "user": {
#             "username": user.username,
#             "email": user.email,
#             "name": user.name,
#             "plan": getattr(user, "plan", None)
#         }
#     }, status=201)

# @csrf_exempt
# @api_view(['POST'])
# def pin_chat(request, username, chat_id):
#     user = User.objects(username=username).first()
#     if not user:
#         return Response({"message": "User not found"}, status=404)
#     pinned_value = request.data.get('pinned', True)
#     # Find chat
#     chat = next((c for c in user.chats if c.chat_id == chat_id), None)
#     if not chat:
#         return Response({"message": "Chat not found"}, status=404)
#     # Set pinned
#     chat.pinned = pinned_value
#     # Mark user as changed so MongoEngine saves embedded document properly
#     user.save()
#     return Response({'status': 'ok', 'chat_id': chat_id, 'pinned': pinned_value})


# @csrf_exempt
# @api_view(["POST"])
# def login_user(request):
#     data = request.data

#     if not data.get("username") or not data.get("password"):
#         return Response({"message": "Username and password required"}, status=400)

#     user = User.objects(username=data["username"]).first()
#     if not user or not user.check_password(data["password"]):
#         return Response({"message": "Invalid credentials"}, status=401)

#     token = create_jwt(user)
#     return Response({
#         "token": token,
#         "user": {"username": user.username, "name": user.name}
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
#             "pinned": getattr(chat, "pinned", False),  # include pinned
#             "messages": [{"text": m.text, "sender": m.sender} for m in chat.messages]
#         }
#         for chat in user.chats
#     ]
#     return Response({"chats": chats_data})


# # Start new chat
# @csrf_exempt
# @api_view(["POST"])
# def start_new_chat(request, username):
#     user = User.objects(username=username).first()
#     if not user:
#         return Response({"message": "User not found"}, status=404)

#     chat_id = str(uuid.uuid4())
#     chat_title = request.data.get("title", f"Chat {len(user.chats)+1}")
#     new_chat = Chat(chat_id=chat_id, title=chat_title, pinned=False)
#     user.chats.append(new_chat)
#     user.save()

#     return Response({"chat_id": chat_id, "title": chat_title})

# # Add message to a chat
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

# # Delete a chat
# @csrf_exempt
# @api_view(["DELETE"])
# def delete_chat(request, username, chat_id):
#     user = User.objects(username=username).first()
#     if not user:
#         return Response({"message": "User not found"}, status=404)

#     chat = next((c for c in user.chats if c.chat_id == chat_id), None)
#     if not chat:
#         return Response({"message": "Chat not found"}, status=404)

#     user.chats = [c for c in user.chats if c.chat_id != chat_id]
#     user.save()
#     return Response({"message": "Chat deleted"})


from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from mongoengine.queryset.visitor import Q
import uuid

from .models import User, Chat, Message
from .jwt import create_jwt

from django.http import JsonResponse
import json
from .rag import query_rag


@csrf_exempt
@api_view(["POST"])
def signup_user(request):
    data = request.data

    email = data.get("email", "").strip().lower()
    password = data.get("password")
    username = data.get("username")
    name = data.get("name", "")
    plan = data.get("plan")

    if not email or not password:
        return Response(
            {"message": "Email and password required"},
            status=400
        )

    # ---- CHECK EMAIL ----
    if User.objects(email=email).first():
        return Response(
            {"message": "An account already exists for this email"},
            status=400
        )

    # ---- CHECK USERNAME ----
    if username:
        if User.objects(username=username).first():
            return Response(
                {"message": "Username already taken"},
                status=400
            )
    else:
        # fallback username from email
        base_username = email.split("@")[0]
        username = base_username
        counter = 1
        while User.objects(username=username).first():
            username = f"{base_username}{counter}"
            counter += 1

    # ---- CREATE USER ----
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

@csrf_exempt
@api_view(["POST"])
def login_user(request):
    data = request.data

    identifier = data.get("identifier", "").strip().lower()
    password = data.get("password")

    if not identifier or not password:
        return Response(
            {"message": "Username/email and password required"},
            status=400
        )

    user = User.objects(
        Q(username=identifier) | Q(email=identifier)
    ).first()

    if not user or not user.check_password(password):
        return Response(
            {"message": "Invalid credentials"},
            status=401
        )

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
            "messages": [
                {"text": m.text, "sender": m.sender}
                for m in chat.messages
            ]
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

    user.chats.append(Chat(
        chat_id=chat_id,
        title=title,
        pinned=False
    ))
    user.save()

    return Response({
        "chat_id": chat_id,
        "title": title
    })

@csrf_exempt
@api_view(["POST"])
def add_message(request, username, chat_id):
    user = User.objects(username=username).first()
    if not user:
        return Response({"message": "User not found"}, status=404)

    chat = next((c for c in user.chats if c.chat_id == chat_id), None)
    if not chat:
        return Response({"message": "Chat not found"}, status=404)

    text = request.data.get("text")
    sender = request.data.get("sender", "user")

    chat.messages.append(Message(text=text, sender=sender))
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
