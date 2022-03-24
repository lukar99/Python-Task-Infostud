from django.urls import path
from ApiApp import views


urlpatterns=[
    path('',views.JobAdsGenericView.as_view(), name='getads'),
    path('city/<str:pk>', views.JobAdsCityGenericView.as_view(), name='jobcity'),
    path('employer/<str:pk>/', views.JobAdsEmployerGenericView.as_view(), name='jobcity'),
]