from uuid import UUID
from ninja import Router, Schema, ModelSchema
from ninja.errors import HttpError
from django.shortcuts import get_object_or_404
from django.db.utils import DatabaseError
from . import models


router = Router()


class IngredientInfo(ModelSchema):
    class Config:
        model = models.Ingredient
        model_fields = "__all__"


class IngredientCreate(Schema):
    id: UUID = None
    name: str


class IngredientUpdate(ModelSchema):
    class Config:
        model = models.Ingredient
        model_fields = ["name"]


@router.get("/ingredients/{ingredient_id}", url_name="ingredients", response=IngredientInfo)
def get_ingredient(request, ingredient_id):
    ingredient = get_object_or_404(models.Ingredient, id=ingredient_id)
    return ingredient


@router.get("/ingredients/", url_name="ingredients", response=list[IngredientInfo])
def list_ingredients(request):
    return models.Ingredient.objects.all()


@router.post("/ingredients/", url_name="ingredients")
def create_ingredient(request, payload: IngredientCreate):
    try:
        ingredient = models.Ingredient.objects.create(**payload.dict())
    except DatabaseError as e:
        raise HttpError(
            status_code=409,
            message=f"An error occurred while inserting into database: {str(e)}",
        )

    return dict(id=ingredient.id)


@router.put("/ingredients/{ingredient_id}", url_name="ingredients")
def update_ingredient(request, ingredient_id, payload: IngredientUpdate):
    ingredient = get_object_or_404(models.Ingredient, id=ingredient_id)

    for field, value in payload.dict().items():
        setattr(ingredient, field, value)
    ingredient.save(update_fields=payload.dict().keys())

    return dict(id=ingredient.id, updated=True)
