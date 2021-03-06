"""recepty_projekt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from recepty_list import views
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.authtoken.views import obtain_auth_token
app_name = 'account'


router = routers.DefaultRouter()
router.register(r"recepty",views.ReceptView,'Recepty')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('login',obtain_auth_token, name = "login")
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    #nepatri to k admin alebo api je to link naviac a preto to pridavame cez plusko
