import os
from rest_framework.viewsets import ModelViewSet
from django.conf import settings
from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

# from .models import Video
from basic_app import models, serializers
from .models import Vehicle
from .serializers import VehicleSerializer
from django.db.models import Count

from rest_framework import filters


def paginate_data(request):
    # Get the values for limit and offset from the GET request parameters
    limit = int(request.GET.get('limit', 10))
    offset = int(request.GET.get('offset', 0))

    # Fetch the data from the database using the limit and offset values
    queryset = YourModel.objects.all()[offset:offset + limit]

    # Serialize the data if needed
    serialized_data = serialize_data(queryset)

    return JsonResponse(serialized_data, safe=False)


# Create your views here.
class List1Mark(generics.ListCreateAPIView):
    queryset = models.Mark.objects.all()
    serializer_class = serializers.MarkSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['mark_name']
    pagination_class = PageNumberPagination


class Detail1Mark(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Mark.objects.all()
    serializer_class = serializers.MarkSerializer
    pagination_class = PageNumberPagination


class List1Model(generics.ListCreateAPIView):
    queryset = models.Model1.objects.all()
    serializer_class = serializers.ModelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['model_name']
    pagination_class = PageNumberPagination


class Detail1Model(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Model1.objects.all()
    serializer_class = serializers.ModelSerializer
    pagination_class = PageNumberPagination


class ListFuel(generics.ListCreateAPIView):
    queryset = models.Fuel1.objects.all()
    serializer_class = serializers.FuelSerializer
    pagination_class = PageNumberPagination
    search_fields = ['fuel']
    filter_backends = [filters.SearchFilter]


class DetailFuel(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Fuel1.objects.all()
    serializer_class = serializers.FuelSerializer
    pagination_class = PageNumberPagination
    search_fields = ['fuel']
    filter_backends = [filters.SearchFilter]


class ListFile(generics.ListCreateAPIView):
    queryset = models.Upload_File.objects.all()
    serializer_class = serializers.FileSerializer
    pagination_class = PageNumberPagination


class DetailFile(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Upload_File.objects.all()
    serializer_class = serializers.FileSerializer
    pagination_class = PageNumberPagination


class ListBody(generics.ListCreateAPIView):
    queryset = models.Body.objects.all()
    serializer_class = serializers.BodySerializer
    search_fields = ['body_of_vehicle']
    filter_backends = [filters.SearchFilter]


class DetailBody(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Body.objects.all()
    serializer_class = serializers.BodySerializer


from rest_framework import viewsets
from .models import MyModel
from .serializers import MyModelSerializer


class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer


from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .models import MyModel
from .serializers import MyModelSerializer


class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

    async def perform_create(self, serializer):
        instance = serializer.save()
        await self.send_websocket_message(instance)

    async def perform_update(self, serializer):
        instance = serializer.save()
        await self.send_websocket_message(instance)

    async def perform_destroy(self, instance):
        await self.send_websocket_message(instance)
        instance.delete()

    async def send_websocket_message(self, instance):
        from channels.layers import get_channel_layer
        channel_layer = get_channel_layer()

        await channel_layer.group_send(
            f'mymodel_{instance.id}',
            {
                'type': 'mymodel_message',
                'message': 'Model instance updated',
            }
        )

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        instance = get_object_or_404(queryset, pk=kwargs['pk'])
        serializer = self.get_serializer(instance)

        return Response(serializer.data)


def video_view(request):
    videos = Video.objects.all()
    return render(request, 'video.html', context={'videos': videos})


class VehicleViewSet(ModelViewSet):
    queryset = Vehicle.objects.values('mark_name').annotate(count=Count('model_name'))
    serializer_class = VehicleSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        data = [{'mark_name': item['mark_name'], 'count': item['count']} for item in queryset]
        return Response(data)


# Пассажирский (LCV)
class VehicleViewSetCategory(ModelViewSet):
    serializer_class = VehicleSerializer

    def get_queryset(self):
        queryset = Vehicle.objects.values('body').annotate(count=Count('model_name'))
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        return Response(queryset)


class LimitOffsetPaginator(LimitOffsetPagination):
    default_limit = 20
    max_limit = 100


class ModelFilterViewSet(ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['model_name', 'mark_name']
    pagination_class = LimitOffsetPaginator


class VehicleSortViewSet(ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['model_name', 'mark_name', 'body', 'fuel']
