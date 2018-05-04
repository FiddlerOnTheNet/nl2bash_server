# url patterns for the myapp application

from django.urls import path
from . import views

# List of URLs to various pages
urlpatterns = [
    path('', views.tester, name='tester'),  # Tester UI
]