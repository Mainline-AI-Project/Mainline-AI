from django.urls import path, include
from apps.users.views import rag_query
from apps.users import views
from django.contrib import admin
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.urls import re_path

urlpatterns = [
    path("api/users/", include("apps.users.urls")),
    path("api/", include("api.urls")),
    path('api/query/', rag_query),
    path("api/auth/forgot-password/", views.forgot_password, name="forgot_password"),
    path("api/auth/reset-password/",  views.reset_password,  name="reset_password"),
    path('admin/', admin.site.urls),
    path('', lambda request: HttpResponse("Backend is running ✅")),
    re_path(r'^$', TemplateView.as_view(template_name="index.html")),
    re_path(r'^(?:.*)/?$', TemplateView.as_view(template_name="index.html")),
]
