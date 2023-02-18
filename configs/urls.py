"""configs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from app.views import userfirst
from rest_framework import routers
from rest_framework.routers import DefaultRouter


from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = DefaultRouter()

router.register('userapi/first', userfirst, basename='user')                #url for operations
router.register('userapi/first/<int:pk>', userfirst, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    
    path('gettoken/', TokenObtainPairView.as_view()),               #url for generation of token valid for 5 mins
    path('refreshtoken/', TokenRefreshView.as_view()),              #url to refresh the token
    path('verifytoken/', TokenVerifyView.as_view()),                #url to check validity of the token
]
