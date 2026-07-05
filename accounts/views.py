from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class CustomUserListView(ListView):
    model = CustomUser


class CustomUserDetailView(DetailView):
    model = CustomUser


class CustomUserCreateView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("accounts:user-list")


class CustomUserUpdateView(UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    success_url = reverse_lazy("accounts:user-list")
