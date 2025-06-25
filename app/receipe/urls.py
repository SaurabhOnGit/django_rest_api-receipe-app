
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from receipe import views

router = DefaultRouter()

router.register('receipes', views.ReceipeViewSet)

app_name = 'receipe'

url_patterns = [
    path('', include(router.urls)),
]