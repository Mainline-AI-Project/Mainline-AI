import jwt
from datetime import datetime, timedelta
from django.conf import settings

def create_jwt(user):
    payload = {
        "user_id": str(user.id),
        "username": user.username,
        "name": user.name,
        "exp": datetime.utcnow() + timedelta(hours=24)
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
