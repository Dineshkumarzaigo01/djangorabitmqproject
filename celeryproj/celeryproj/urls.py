"""
URL configuration for celeryproj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from firstapp.views import index,multiply,webhook_send_info # add this


urlpatterns = [
    path('admin/', admin.site.urls),
    path('send-email/', index, name='send_email'),
    path('multiply/', multiply, name='  multiply'),
    path('webhook_send_info',webhook_send_info, name='webhook_send_info')
    
]
