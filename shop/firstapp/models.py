from django.db import models

# Create your models here.
class Shop(models.Model):
    shop_id = models.AutoField(primary_key=True)
    shop_name = models.CharField(max_length=100, blank=True, null=True)
    shop_desc = models.CharField(max_length=100, blank=True, null=True)
    rest_date = models.CharField(max_length=100, blank=True, null=True)
    parking_info = models.CharField(max_length=100, blank=True, null=True)
    img_path = models.CharField(max_length=255, blank=True, null=True)

    class Meta: 
        managed = False
        db_table = 'shop'