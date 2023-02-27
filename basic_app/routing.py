from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/mymodel/<int:mymodel_id>/', consumers.MyModelConsumer.as_asgi()),
]
