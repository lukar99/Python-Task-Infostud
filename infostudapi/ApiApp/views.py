from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import GenericAPIView

from rest_framework import mixins

from ApiApp.models import JobAds
from ApiApp.serializers import AdsSerializer


class JobAdsGenericView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):  # Decided to use generic-view for automatic django-restframework pagination
    queryset = JobAds.objects.all()
    serializer_class = AdsSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
