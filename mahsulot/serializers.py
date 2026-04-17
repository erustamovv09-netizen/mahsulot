from rest_framework import serializers
from .models import Mahsulot


class MahsulotSerializer(serializers.ModelSerializer):
    image = serializers.CharField(required=True)
    class Meta:
        model = Mahsulot
        fields = "__all__"