from uuid import UUID
from ninja import Router, Schema, ModelSchema
from ninja.errors import HttpError
from django.shortcuts import get_object_or_404
from django.db.utils import DatabaseError
from . import models


router = Router()


class RecipeInfo(ModelSchema):
    class Config:
        model = models.Recipe
        model_fields = "__all__"


class RecipeCreate(Schema):
    id: UUID = None
    name: str
    description: str
    instructions: str


class RecipeUpdate(ModelSchema):
    class Config:
        model = models.Recipe
        model_fields = ["name", "description", "instructions"]


@router.get("/recipes/{recipe_id}", url_name="recipes", response=RecipeInfo)
def get_recipe(request, recipe_id):
    recipe = get_object_or_404(models.Recipe, id=recipe_id)
    return recipe


@router.get("/recipes/", url_name="recipes", response=list[RecipeInfo])
def list_recipes(request):
    return models.Recipe.objects.all().order_by("-created")


@router.post("/recipes/", url_name="recipes")
def create_recipe(request, payload: RecipeCreate):
    try:
        recipe = models.Recipe.objects.create(**payload.dict())
    except DatabaseError as e:
        raise HttpError(
            status_code=409,
            message=f"An error occurred while inserting into database: {str(e)}",
        )

    return dict(id=recipe.id)


@router.put("/recipes/{recipe_id}", url_name="recipes")
def update_recipe(request, recipe_id, payload: RecipeUpdate):
    recipe = get_object_or_404(models.Recipe, id=recipe_id)

    for field, value in payload.dict().items():
        setattr(recipe, field, value)
    recipe.save(update_fields=payload.dict().keys())

    return dict(id=recipe.id, updated=True)
