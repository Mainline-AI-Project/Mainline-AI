from django.urls import path
from .views import signup_user, login_user, get_chats, start_new_chat, add_message,delete_chat, pin_chat
from . import views

urlpatterns = [
    path("signup/", signup_user),
    path("login/", login_user),
    path("chats/<str:username>/", get_chats),
    path("chats/<str:username>/new/", start_new_chat),
    path("chats/<str:username>/<str:chat_id>/add/", add_message),
    path("chats/<str:username>/<str:chat_id>/delete/", delete_chat),
    path('chats/<str:username>/<str:chat_id>/pin/', pin_chat),
    path('api/query/', views.rag_query),
]
