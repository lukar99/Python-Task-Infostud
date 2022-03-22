from django.urls import path
from ApiApp import views


urlpatterns=[
    path('getads/',views.JobAdsGenericView.as_view(), name='getads')
]