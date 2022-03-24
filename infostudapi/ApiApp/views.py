from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import GenericAPIView

from rest_framework import mixins, generics, filters

from ApiApp.models import JobAds
from ApiApp.serializers import AdsSerializer


class JobAdsGenericView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):  # Decided to use generic-view for automatic django-restframework pagination
    queryset = JobAds.objects.all()
    serializer_class = AdsSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class JobAdsCityGenericView(generics.ListAPIView):
    serializer_class = AdsSerializer

    def get_queryset(self):
        city = self.kwargs['pk']
        return JobAds.objects.filter(job_address__contains=city) # added __contains method to enlist ads with multiple job addresses

class JobAdsEmployerGenericView(generics.ListAPIView):
    serializer_class = AdsSerializer

    def get_queryset(self):
        employer = self.kwargs['pk']
        return JobAds.objects.filter(employer__contains=employer)
        