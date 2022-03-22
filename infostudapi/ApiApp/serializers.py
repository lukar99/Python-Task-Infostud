import imp
from rest_framework import serializers
from ApiApp.models import JobAds

class AdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobAds
        fields = '__all__'