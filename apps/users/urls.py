from django.urls import path

from .views import user_login_view
from .views import user_logout_view
from .views import user_password_change_done_view
from .views import user_password_change_view
from .views import user_password_reset_complete_view
from .views import user_password_reset_confirm_view
from .views import user_password_reset_done_view
from .views import user_password_reset_view
from .views import user_detail_view
from .views import user_redirect_view
from .views import user_update_view

app_name = "users"
urlpatterns = [
    path("login/", view=user_login_view, name="login"),
    path("logout/", view=user_logout_view, name="logout"),
    path("password/change/", view=user_password_change_view, name="password_change"),
    path(
        "password/change/done/",
        view=user_password_change_done_view,
        name="password_change_done",
    ),
    path("password/reset/", view=user_password_reset_view, name="password_reset"),
    path(
        "password/reset/done/",
        view=user_password_reset_done_view,
        name="password_reset_done",
    ),
    path(
        "password/reset/<uidb64>/<token>/",
        view=user_password_reset_confirm_view,
        name="password_reset_confirm",
    ),
    path(
        "password/reset/complete/",
        view=user_password_reset_complete_view,
        name="password_reset_complete",
    ),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<int:pk>/", view=user_detail_view, name="detail"),
]
