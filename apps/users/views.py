from __future__ import annotations

from typing import TYPE_CHECKING

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import PasswordChangeDoneView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordResetCompleteView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth import logout
from django.urls import reverse
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView
from django.views.generic import RedirectView
from django.views.generic import UpdateView

from apps.users.models import User

if TYPE_CHECKING:
    from django.db.models import QuerySet


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "id"
    slug_url_kwarg = "id"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = ["name"]
    success_message = _("Information successfully updated")

    def get_success_url(self) -> str:
        assert self.request.user.is_authenticated  # type guard
        return self.request.user.get_absolute_url()

    def get_object(self, queryset: QuerySet | None = None) -> User:
        assert self.request.user.is_authenticated  # type guard
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self) -> str:
        return reverse("users:detail", kwargs={"pk": self.request.user.pk})


user_redirect_view = UserRedirectView.as_view()


class UserLoginView(LoginView):
    template_name = "users/login.html"


user_login_view = UserLoginView.as_view()


def user_logout_view(request):
    logout(request)
    return redirect("home")


user_password_change_view = PasswordChangeView.as_view(
    template_name="users/password_change.html",
    success_url=reverse_lazy("users:password_change_done"),
)

user_password_change_done_view = PasswordChangeDoneView.as_view(
    template_name="users/password_change_done.html",
)

user_password_reset_view = PasswordResetView.as_view(
    template_name="users/password_reset.html",
    email_template_name="users/password_reset_email.txt",
    success_url=reverse_lazy("users:password_reset_done"),
)

user_password_reset_done_view = PasswordResetDoneView.as_view(
    template_name="users/password_reset_done.html",
)

user_password_reset_confirm_view = PasswordResetConfirmView.as_view(
    template_name="users/password_reset_confirm.html",
    success_url=reverse_lazy("users:password_reset_complete"),
)

user_password_reset_complete_view = PasswordResetCompleteView.as_view(
    template_name="users/password_reset_complete.html",
)
