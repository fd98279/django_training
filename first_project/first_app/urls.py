from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('post_test', views.post_test, name='post_test'),
    path('add_post', views.add_post, name='add_post'),
    path('static_test', views.static_test, name='post_test'),
]
