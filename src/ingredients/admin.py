from django.contrib import admin

from .models import Ingredient


class IngredientAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


admin.site.register(Ingredient, IngredientAdmin)
