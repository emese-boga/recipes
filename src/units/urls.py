from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import UnitListView


router = SimpleRouter(trailing_slash=True)

urlpatterns = [
    path("", view=UnitListView.as_view(), name="get_units"),
]
