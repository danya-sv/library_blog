from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    UNITS = [
        ("g", "граммы"),
        ("kg", "килограммы"),
        ("ml", "миллилитры"),
        ("l", "литры"),
        ("pcs", "штуки"),
    ]

    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    unit = models.CharField(max_length=10, choices=UNITS)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
    is_optional = models.BooleanField(default=False)
    calories = models.PositiveIntegerField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.quantity} {self.unit})"

class Collection(models.Model):
    name = models.CharField(max_length=200)
    recipes = models.ManyToManyField(Recipe, related_name='collections')

    def __str__(self):
        return self.name