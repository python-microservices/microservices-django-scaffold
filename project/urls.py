"""project URL Configuration

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

Try a private URL
curl -X POST http://127.0.0.1:8000/api-token-auth/ -d '{"username": "admin", "password": "test1234"}' -H "Content-Type: application/json"
curl -X GET http://127.0.0.1:8000/example-private/ -H 'Authorization: Token 3f8c6c1ed1eec35a59785f6d1963bf69ac633119'
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views

from template.views import ColorViewSet, ColorList, ColorDetail, ExampleView

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('template', ColorViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('template2/', ColorList.as_view()),
    path('template2/<str:pk>/', ColorDetail.as_view()),
    path('example-private/', ExampleView.as_view()),
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
