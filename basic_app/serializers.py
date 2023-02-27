from rest_framework import serializers
from rest_framework import serializers
from .models import MyModel
from basic_app import models


class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mark
        fields = '__all__'


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Model1
        fields = '__all__'


class FuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fuel1
        fields = '__all__'


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Upload_File
        fields = '__all__'


class BodySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Body
        fields = '__all__'


class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = '__all__'
