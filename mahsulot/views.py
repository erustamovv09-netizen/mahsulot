from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Mahsulot
from .serializers import MahsulotSerializer


class MahsulotViewSet(ModelViewSet):
    queryset = Mahsulot.objects.all()
    serializer_class = MahsulotSerializer

    def create(self, request, *args, **kwargs):
        is_many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=is_many)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)