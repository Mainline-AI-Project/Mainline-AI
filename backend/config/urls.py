from django.urls import path, include
from apps.users.views import rag_query

urlpatterns = [
    path("api/users/", include("apps.users.urls")),
    path("api/", include("api.urls")),
    path('api/query/', rag_query),
]
