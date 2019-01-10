from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
	"""trial serializer
	"""
	class Meta:
		model = Movie
		fields = (
			'id',
			'title',
			'desc',
			'year',
		)