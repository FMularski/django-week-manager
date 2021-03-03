from django.urls import  path
from . import views 

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('update/', views.update, name='update')
]
