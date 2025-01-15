from rest_framework import serializers
from .models import Item, job_post

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = job_post
        fields = '__all__'