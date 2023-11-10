from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import IngredientCreateListView, IngredientView


router = SimpleRouter(trailing_slash=True)

urlpatterns = [
    path("", view=IngredientCreateListView.as_view(), name="ingredients_list_create"),
    path("<uuid:id>", view=IngredientView.as_view(), name="ingredients"),
]
