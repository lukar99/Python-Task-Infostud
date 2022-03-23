from django.urls import path
from ApiApp import views


urlpatterns=[
    path('getads/',views.JobAdsGenericView.as_view(), name='getads'),
    path('getads/city/<str:pk>', views.JobAdsCityGenericView.as_view(), name='jobcity'),
    path('getads/employer/<str:pk>/', views.JobAdsEmployerGenericView.as_view(), name='jobcity'),
]