from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Movie


class MovieAdmin(admin.ModelAdmin):
	"""movie admin
	"""
	model = Movie
	fields = (
		'title',
		'desc',
		'year',
	)

admin.site.register(Movie, MovieAdmin)
