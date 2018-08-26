from django.shortcuts import render
from rest_framework import generics
from .models import Songs
from .serializer import SongSerializer
# Create your views here.

class ListSongsView(generics.ListAPIView):
    queryset = Songs.objects.all()
    serializer_class = SongSerializer


