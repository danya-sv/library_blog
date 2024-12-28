from django import forms
from recipes.models import Recipe, Ingredient, Collection
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description']

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity', 'unit', 'is_optional', 'calories', 'notes']

class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ['name']