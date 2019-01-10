from django.db import models


class Movie(models.Model):
	"""movie
	"""
	title = models.CharField(max_length=100)
	desc = models.TextField(blank=True)
	year = models.IntegerField()


