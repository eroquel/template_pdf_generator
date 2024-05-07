from rest_framework import serializers
from .models import Plantilla

class PlantillasSerializer(serializers.ModelSerializer):
  class Meta:
    model = Plantilla
    fields = ("id","template_name","template_url")