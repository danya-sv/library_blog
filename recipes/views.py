from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.edit import FormView
from .models import Recipe, Ingredient, Collection
from .forms import RecipeForm, IngredientForm, CollectionForm

class RecipeListView(ListView):
    model = Recipe
    template_name = "recipes/recipe_list.html"
    context_object_name = "recipes"

    def get_queryset(self):
        return Recipe.objects.all().order_by("-id")

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipes/recipe_detail.html"
    context_object_name = "recipe"
    pk_url_kwarg = 'recipe_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = self.get_object()
        context['total_calories'] = sum(ingredient.calories or 0 for ingredient in recipe.ingredients.all())
        return context

class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "recipes/add_recipe.html"

    def get_success_url(self):
        return reverse_lazy('recipe_list')

class IngredientCreateView(FormView):
    form_class = IngredientForm
    template_name = "recipes/add_ingredient.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe'] = get_object_or_404(Recipe, id=self.kwargs['recipe_id'])
        return context

    def form_valid(self, form):
        recipe = get_object_or_404(Recipe, id=self.kwargs['recipe_id'])
        ingredient = form.save(commit=False)
        ingredient.recipe = recipe
        ingredient.save()
        return redirect('recipe_detail', recipe_id=recipe.id)

class RecipeDeleteView(DeleteView):
    model = Recipe
    success_url = reverse_lazy('recipe_list')
    pk_url_kwarg = 'recipe_id'

class IngredientUpdateView(UpdateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = "recipes/edit_ingredient.html"
    pk_url_kwarg = 'ingredient_id'

    def get_success_url(self):
        return reverse_lazy('recipe_detail', kwargs={'recipe_id': self.object.recipe.id})

class CollectionListView(ListView):
    model = Collection
    template_name = "recipes/collection_list.html"
    context_object_name = "collections"

class CollectionCreateView(CreateView):
    model = Collection
    form_class = CollectionForm
    template_name = "recipes/add_collection.html"

    def get_success_url(self):
        return reverse_lazy('collection_list')

class CollectionDetailView(DetailView):
    model = Collection
    template_name = "recipes/collection_detail.html"
    context_object_name = "collection"
    pk_url_kwarg = 'collection_id'