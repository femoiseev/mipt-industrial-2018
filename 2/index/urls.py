from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('delete/<td_id>', views.delete, name='delete'),
    path('deleteall', views.deleteall, name='deleteall'),
    path('complete/<td_id>', views.complete, name='complete'),
    path('deletecomplete', views.deletecomplete, name='deletecomplete')
]