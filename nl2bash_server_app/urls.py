# url patterns for the myapp application

from django.urls import path
from . import views

# List of URLs to various pages
urlpatterns = [
    path('', views.tester_init, name='tester_init'),  # Init
    path('tester', views.tester, name='tester'),  # Tester UI
    path('submit', views.submit, name='submit'),  # Submit button
    path('skip', views.skip, name='skip'),  # Skip button
]
