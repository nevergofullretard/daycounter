from django.db import models
from django.utils import timezone



class DateTimeData(models.Model):
	name = models.CharField(max_length=50)
	datetime = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return f'{self.name}'

#class Images(models.Model):
	#name = models.CharField(max_length=50, default='image')
	#picture = models.ImageField(upload_to='images')

