from django.urls import path, include
from rest_framework import routers

from .views import ListPlantillasAPIView, GeneratePDf

router = routers.DefaultRouter()
router.register(r'plantillas', ListPlantillasAPIView)

urlpatterns = [
  path('', include(router.urls)),
  path('generate-pdf/', GeneratePDf),
  # path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]