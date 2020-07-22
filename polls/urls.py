from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('result', views.index, name='index')
]