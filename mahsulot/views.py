from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Mahsulot  # Mashina so'zini Mahsulotga almashtirdim
from .serializers import MahsulotSerializer # Serializer ham Mahsulot bo'lishi kerak

class MahsulotViewSet(viewsets.ModelViewSet):
    queryset = Mahsulot.objects.all()
    serializer_class = MahsulotSerializer
    # Rasm yuklash uchun parserlar
    parser_classes = (MultiPartParser, FormParser)