from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

LEVEL = (
    ("Ниже Junior", "Ниже Junior"),
    ("Junior", "Junior"),
    ("Middle", "Middle"),
    ("Senior", "Senior"),
)


class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")
    phone_number = forms.CharField(required=True, label="Phone number")
    age = forms.IntegerField(required=True, label="Age")
    level = forms.ChoiceField(required=True, choices=LEVEL, label="Level")

    class Meta:
        model = models.CustomUser
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "age",
            "phone_number",
            "level",
        )

        def save(self, commit=True):
            user = super(CustomRegisterForm, self).save(commit=False)
            user.email = self.cleaned_data["email"]
            user.phone_number = self.cleaned_data["phone_number"]
            user.age = self.cleaned_data["age"]
            user.level = self.cleaned_data["level"]

            if commit:
                user.save()
            return user
