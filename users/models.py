from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):
    LEVEL = (
        ("Ниже Junior", "Ниже Junior"),
        ("Junior", "Junior"),
        ("Middle", "Middle"),
        ("Senior", "Senior"),
    )

    phone_number = models.CharField(max_length=14)
    level = models.CharField(max_length=20, choices=LEVEL)
    age = models.PositiveIntegerField(default=18)
    salary = models.CharField(max_length=50, default="Зарплата не определена")

    def save(self, *args, **kwargs):
        if self.level == "Ниже Junior":
            self.salary = "Пожалуйста, улучшите свои навыки и попробуйте снова."
        elif self.level == "Junior":
            self.salary = "700$"
        elif self.level == "Middle":
            self.salary = "1000$"
        elif self.level == "Senior":
            self.salary = "2000$"
        else:
            self.salary = (
                "Указанный уровень нам не понятен. К сожалению, вы нам не подходите."
            )

        super().save(*args, **kwargs)
