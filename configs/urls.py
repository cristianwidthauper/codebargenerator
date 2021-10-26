from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from pesquisa.views import UrnaViewSet

router = routers.DefaultRouter()
router.register(r'urnas', UrnaViewSet, 'urna')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
