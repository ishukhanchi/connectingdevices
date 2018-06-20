from django.db import models

# Create your models here.
class  Device():
 	pass Device(models.Model):
	id = models.IntegerField(max_length=20)
    api = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
