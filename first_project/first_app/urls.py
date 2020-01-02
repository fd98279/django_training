from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('post_test', views.post_test, name='post_test'),
    path('add_post', views.add_post, name='add_post'),
    path('static_test', views.static_test, name='post_test'),

    # Class based views
    path('destinations', views.DestinationList.as_view(), name='destination_list'),
    path('destinations/<int:pk>', views.DestinationDetail.as_view(), name='destination_detail'),
    path('create', views.DestinationCreate.as_view(), name='destination_create'),
    path('update/<int:pk>', views.DestinationUpdate.as_view(), name='destination_update'),
    path('delete/<int:pk>', views.DestinationDelete.as_view(), name='destination_delete'),

    # Function based views
    path('destinationslist', views.Destination_list, name='destination_list1'),
    path('destinationscreate', views.Destination_create, name='destination_new1'),
    path('destinationsedit/<int:pk>', views.Destination_update, name='destination_edit1'),
    path('destinationsdelete/<int:pk>', views.Destination_delete, name='destination_delete1'),

    # Forms register
    path('register', views.regform, name = 'registration form'),

    # DRF
    path('drf/', views.API_objects.as_view()),
    path('drf/<int:pk>/', views.API_objects_details.as_view()),
]
