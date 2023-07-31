from os import environ
from ninja import NinjaAPI


api = NinjaAPI(
    title="Recipes APi",
    description="Recipes operations",
    version=environ.get("VERSION"),
    urls_namespace="api",
)


@api.get("healthcheck/")
def healthcheck(request):
    return dict(success=True)
