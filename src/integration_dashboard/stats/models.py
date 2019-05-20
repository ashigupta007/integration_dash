from django.db import models

# Create your models here.
class DailyCrashReport(models.Model):
	reportdate = models.CharField(max_length =20,)
	reporttime = models.CharField(max_length=20,)
	noofcrashes =models.IntegerField(max_length = 20,)

