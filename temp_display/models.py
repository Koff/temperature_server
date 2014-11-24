from django.db import models


class Temps(models.Model):
    time_stamp = models.DateTimeField(primary_key=True)
    temperature = models.DecimalField(max_digits=23, decimal_places=8)
    comments = models.CharField(max_length=160)
    extra = models.CharField(max_length=1)