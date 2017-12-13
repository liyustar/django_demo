from django.db import models

# Create your models here.

class FundInfo(models.Model):
    id = models.AutoField(primary_key=True)
    symbol = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    wave3 = models.DecimalField(max_digits=18, decimal_places=6)
    wave_evaluate3 = models.DecimalField(max_digits=18, decimal_places=6)
    risk3 = models.DecimalField(max_digits=18, decimal_places=6)
    risk_evaluate3 = models.DecimalField(max_digits=18, decimal_places=6)
    sharp3 = models.DecimalField(max_digits=18, decimal_places=6)
    sharp_evaluate3 = models.DecimalField(max_digits=18, decimal_places=6)
    return_rate = models.DecimalField(max_digits=18, decimal_places=6) # return
    rank = models.IntegerField()
    update_time = models.DateTimeField()

    def __str__(self):
        return self.text