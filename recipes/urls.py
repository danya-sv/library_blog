from django.urls import path
from . import views

urlpatterns = [
    path('recipe_list/', views.RecipeListView.as_view(), name='recipe_list'),
    path('recipe/<int:recipe_id>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/add/', views.RecipeCreateView.as_view(), name='add_recipe'),
    path('recipe/<int:recipe_id>/add-ingredient/', views.IngredientCreateView.as_view(), name='add_ingredient'),
    path('recipe/<int:recipe_id>/delete/', views.RecipeDeleteView.as_view(), name='delete_recipe'),
    path('ingredient/<int:ingredient_id>/edit/', views.IngredientUpdateView.as_view(), name='edit_ingredient'),
    path('collections/', views.CollectionListView.as_view(), name='collection_list'),
    path('collections/add/', views.CollectionCreateView.as_view(), name='add_collection'),
    path('collections/<int:collection_id>/', views.CollectionDetailView.as_view(), name='collection_detail'),
]