from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('ads/', views.ListCreateAds.as_view()),
    path('ads/<int:pk>', views.RetriveEditDelete.as_view()),
    path('display-industry/<str:pk>', views.DisplayIndustry.as_view()),
    path('users/', views.ListCreateUser.as_view()),
    path('get-token/', obtain_auth_token),
    path('create-user/', views.CreateUser.as_view())
]