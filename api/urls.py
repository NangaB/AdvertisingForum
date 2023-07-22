from django.urls import path
from . import views

urlpatterns = [
    path('ads/', views.ListCreateAds.as_view()),
    path('ads/<int:pk>', views.RetriveEditDelete.as_view()),
    path('display-industry/<str:pk>', views.DisplayIndustry.as_view()),
]