from django.shortcuts import render
from .models import Movie
from rest_framework import viewsets
from .serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
	"""trial view set
	"""
	queryset = Movie.objects.all()
	serializer_class = MovieSerializer


