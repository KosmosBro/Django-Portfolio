from django.urls import path

from .api_views import CompanyListAPIView

urlpatterns = [
    path('company/', CompanyListAPIView.as_view(), name='company')
]
