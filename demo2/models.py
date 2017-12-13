from django.db import models

# Create your models here.

class FundInfo(models.Model):
    id = models.AutoField(primary_key=True)
    symbol = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    wave3 = models.FloatField(null=True)
    wave_evaluate3 = models.FloatField(null=True)
    risk3 = models.FloatField(null=True)
    risk_evaluate3 = models.FloatField(null=True)
    sharp3 = models.FloatField(null=True)
    sharp_evaluate3 = models.FloatField(null=True)
    return_rate = models.FloatField(null=True) # return
    rank = models.IntegerField(null=True)
    update_time = models.DateTimeField(null=True)

    def __str__(self):
        return self.text