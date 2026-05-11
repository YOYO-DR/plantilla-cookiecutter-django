from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.forms import CharField
from django.forms import EmailField
from django.forms import EmailInput
from django.forms import Form
from django.forms import PasswordInput
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import User


class UserAdminChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User
        field_classes = {"email": EmailField}


class UserAdminCreationForm(admin_forms.AdminUserCreationForm):
    """
    Form for User Creation in the Admin Area.
    """

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User
        fields = ("email",)
        field_classes = {"email": EmailField}
        error_messages = {
            "email": {"unique": _("This email has already been taken.")},
        }


class UserSignupForm(Form):
    email = EmailField(widget=EmailInput(attrs={"autofocus": True}))
    password1 = CharField(widget=PasswordInput)
    password2 = CharField(widget=PasswordInput)

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if get_user_model().objects.filter(email=email).exists():
            raise ValidationError(_("This email has already been taken."))
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(_("The two password fields didn't match."))
        return cleaned_data
