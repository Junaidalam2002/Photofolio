from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('gallery/<str:category>/', views.gallery, name='gallery')
]