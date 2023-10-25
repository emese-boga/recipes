from os import environ
from ninja import NinjaAPI

from recipes.api import router as recipes_router
from ingredients.api import router as ingredients_router


api = NinjaAPI(
    title="Recipes API",
    description="Operations on recipes",
    version=environ.get("VERSION"),
    urls_namespace="api",
)
api.add_router(prefix="", router=recipes_router)
api.add_router(prefix="", router=ingredients_router)


@api.get("healthcheck/")
def healthcheck(request):
    return dict(success=True)
