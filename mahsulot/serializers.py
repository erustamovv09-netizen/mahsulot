from rest_framework import serializers
from .models import Mahsulot

class MahsulotSerializer(serializers.ModelSerializer):
    # CharField o'rniga ImageField ishlatamiz
    image = serializers.ImageField(required=True) 

    class Meta:
        model = Mahsulot
        fields = "__all__"