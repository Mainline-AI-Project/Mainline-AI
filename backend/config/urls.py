from django.urls import path, include
from apps.users.views import rag_query
from apps.users import views

urlpatterns = [
    path("api/users/", include("apps.users.urls")),
    path("api/", include("api.urls")),
    path('api/query/', rag_query),
    path("api/auth/forgot-password/", views.forgot_password, name="forgot_password"),
    path("api/auth/reset-password/",  views.reset_password,  name="reset_password"),
]
