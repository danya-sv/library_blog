from django.contrib import admin
from recipes.models import Recipe, Ingredient, Collection

admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Collection)

