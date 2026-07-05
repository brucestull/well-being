from django.urls import path

from .views import (
    CustomUserCreateView,
    CustomUserDetailView,
    CustomUserListView,
    CustomUserUpdateView,
)

app_name = "accounts"

urlpatterns = [
    path("users/", CustomUserListView.as_view(), name="user-list"),
    path("users/create/", CustomUserCreateView.as_view(), name="user-create"),
    path("users/<int:pk>/", CustomUserDetailView.as_view(), name="user-detail"),
    path("users/<int:pk>/update/", CustomUserUpdateView.as_view(), name="user-update"),
]
