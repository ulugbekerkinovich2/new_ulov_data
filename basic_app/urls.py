from django.urls import path

from basic_app import views

urlpatterns = [
    path('mark/', views.List1Mark.as_view()),
    path('mark/<int:pk>', views.Detail1Mark.as_view()),
    path('model/', views.List1Model.as_view()),
    path('model/<int:pk>', views.Detail1Model.as_view()),
    path('fuel/', views.ListFuel.as_view()),
    path('fuel/<int:pk>', views.DetailFuel.as_view()),
    path('file/', views.ListFile.as_view()),
    path('file/<int:pk>', views.DetailFile.as_view())

]
