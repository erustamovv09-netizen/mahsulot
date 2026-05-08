from django.db import models
from django.utils import timezone # Vaqt bilan ishlash uchun

class Mahsulot(models.Model):
    # Mashina asosiy ma'lumotlari
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    transmission = models.CharField(max_length=50)
    engine_volume = models.CharField(max_length=50)
    year = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    
    # RASM
    image = models.ImageField(upload_to='cars/', null=True, blank=True)

    # Kontakt ma'lumotlari
    owner_phone = models.CharField(max_length=20, default="+998901234567")
    telegram_user = models.CharField(max_length=100, default="Rustamovv_E")
    instagram_user = models.CharField(max_length=100, default="rustamovv.09")

    # YANGI QO'SHILGAN QATORLAR (Tahrirlash va xavfsizlik uchun)
    created_at = models.DateTimeField(default=timezone.now) # Qachon qo'shilgani
    secret_key = models.CharField(max_length=100, blank=True, null=True) # Egasining maxfiy kaliti

    def __str__(self):
        return f"{self.name} - {self.owner_phone}"

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"