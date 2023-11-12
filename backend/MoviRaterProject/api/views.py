from django.shortcuts import render
from rest_framework import viewsets
from api.models import Movie,Rating
from api.serializer import MovieSerializer,RatingSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer 
