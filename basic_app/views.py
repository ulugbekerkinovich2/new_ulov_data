from django.shortcuts import render
from rest_framework import generics, filters

from basic_app import models, serializers


# Create your views here.
class List1Mark(generics.ListCreateAPIView):
    queryset = models.Mark.objects.all()
    serializer_class = serializers.MarkSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['mark_name']


class Detail1Mark(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Mark.objects.all()
    serializer_class = serializers.MarkSerializer


class List1Model(generics.ListCreateAPIView):
    queryset = models.Model1.objects.all()
    serializer_class = serializers.ModelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['model_name']


class Detail1Model(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Model1.objects.all()
    serializer_class = serializers.ModelSerializer


class ListFuel(generics.ListCreateAPIView):
    queryset = models.Fuel1.objects.all()
    serializer_class = serializers.FuelSerializer


class DetailFuel(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Fuel1.objects.all()
    serializer_class = serializers.FuelSerializer


class ListFile(generics.ListCreateAPIView):
    queryset = models.Upload_File.objects.all()
    serializer_class = serializers.FileSerializer


class DetailFile(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Upload_File.objects.all()
    serializer_class = serializers.FileSerializer
