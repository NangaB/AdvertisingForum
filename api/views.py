from django.shortcuts import render
from rest_framework.views import APIView
from ads.models import Advertisement
from .serializer import AdSerializer, UserSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from django.http.response import Http404


class ListCreateAds(APIView):
    def get(self, request):
        print('nice view')
        ads = Advertisement.objects.all()
        serializer = AdSerializer(ads, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        print('here')
        serializer = AdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=User.objects.get(is_staff = True))
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RetriveEditDelete(APIView):
    def get_object(self, pk):
        try:
            return Advertisement.objects.get(pk=pk)
        except Advertisement.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        ad = self.get_object(pk)
        serializer = AdSerializer(instance=ad)
        return Response(serializer.data)
    
    def put(self, request, pk):
        ad = self.get_object(pk)
        #check user
        serializer = AdSerializer(instance=ad, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        ad = self.get_object(pk)
        ad.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class DisplayIndustry(APIView):
    def get(self, request, pk):
        try:
            ads = Advertisement.objects.filter(industry=pk)
            if ads.count() != 0:
                serializer = AdSerializer(instance=ads, many=True)
                return Response(data=serializer.data)
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)
        except ads.doesNotExist:
            raise Http404
        else:
            serializer = AdSerializer(instance=ads, many=True)
            return Response(data=serializer.data)
        
class ListCreateUser(APIView):
    def get(self, request):
        if request.user.is_staff:
            users = User.objects.all()
            serializer = UserSerializer(instance=users, many=True)
            return Response(serializer.data)
        else:
            return Response({'response' : "You do not have permission to get this data"})

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)