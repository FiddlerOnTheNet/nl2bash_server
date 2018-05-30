"""djangoprojectt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.views.generic import RedirectView
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

# Default:
urlpatterns = [
    path('admin/', admin.site.urls),
]

# Additional patterns for the app we are creating
urlpatterns += [
    path('nl2bash_server_app/', include('nl2bash_server_app.urls')),
]

# Redirect the root URL of the project to nl2bash_server_app, which
# makes sense to do since nl2bash_server_app is the main (and only)
# app in this project
urlpatterns += [
    path('', RedirectView.as_view(url='/nl2bash_server_app/')),
]

# Enable serving static files
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
