from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("recipes", include("recipes.urls")),
    path("ingredients", include("ingredients.urls")),
    path("units", include("units.urls")),
]
