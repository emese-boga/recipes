from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .models import Unit
from .serializers import UnitSerializer


class UnitListView(ListAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
