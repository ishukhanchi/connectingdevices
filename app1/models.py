from django.db import models

# Create your models here.
class  Device(models.Model):
	id = models.IntegerField(primary_key='true')
	api = models.CharField(max_length=200)
	status = models.CharField(max_length=200)

	def __str__(self):
		return self.id

	def __str__(self):
		return self.api

	def __str__(self):
		return self.status






	