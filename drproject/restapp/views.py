from django.shortcuts import render
from .models import Item , job_post
from .serializers import ItemSerializer , JobSerializer
from rest_framework import generics

class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class UploadJob(generics.ListCreateAPIView):
    queryset = job_post.objects.all()
    serializer_class = JobSerializer