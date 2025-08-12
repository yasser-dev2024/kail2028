from django.urls import path
from . import views

app_name = 'stables'

urlpatterns = [
    path('', views.home, name='home'),
]
