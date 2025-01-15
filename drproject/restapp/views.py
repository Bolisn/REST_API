from django.shortcuts import render
from django.http import HttpResponse
from .models import Item , job_post
from .serializers import ItemSerializer , JobSerializer
from rest_framework import generics

def home(request):
    return render(request, 'home1.html')

class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class UploadJob(generics.ListCreateAPIView):
    queryset = job_post.objects.all()
    serializer_class = JobSerializer