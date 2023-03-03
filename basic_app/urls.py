from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from graphene_django.views import GraphQLView
from basic_app import views
from basic_app.schema import schema

urlpatterns = [
    path('mark/', views.List1Mark.as_view()),
    path('mark/<int:pk>', views.Detail1Mark.as_view()),
    path('model/', views.List1Model.as_view()),
    path('model/<int:pk>', views.Detail1Model.as_view()),
    path('fuel/', views.ListFuel.as_view()),
    path('fuel/<int:pk>', views.DetailFuel.as_view()),
    path('files/', views.ListFile.as_view()),
    path('files/<int:pk>', views.DetailFile.as_view()),
    path('body/', views.ListBody.as_view()),
    path('body/<int:pk>', views.DetailBody.as_view()),
    path('graphql/', GraphQLView.as_view(schema=schema, graphiql=True)),
    path('video/', views.video_view)
]
urlpatterns += [
                  # ...
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
