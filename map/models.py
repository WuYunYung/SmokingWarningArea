from django.db import models
from django.utils import timezone
# Create your models here.


class Address(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()
    pub_date = models.DateTimeField(default=timezone.now)


# longitude精度
# latitude纬度
