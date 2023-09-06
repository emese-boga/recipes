from os import environ
from ninja import NinjaAPI

from recipes.api import router as recipes_router


api = NinjaAPI(
    title="Recipes API",
    description="Operations on recipes",
    version=environ.get("VERSION"),
    urls_namespace="api",
)
api.add_router(prefix="", router=recipes_router)


@api.get("healthcheck/")
def healthcheck(request):
    return dict(success=True)
