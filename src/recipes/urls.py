from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import RecipeCreateListView, RecipeView


router = SimpleRouter(trailing_slash=True)

urlpatterns = [
    path("", view=RecipeCreateListView.as_view(), name="recipes_list_create"),
    path("<uuid:id>", view=RecipeView.as_view(), name="recipes"),
]
