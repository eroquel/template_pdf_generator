from django.db import models

# Create your models here.
class Plantilla(models.Model):
  template_name = models.CharField(max_length=100, unique=True, null=False, blank=False)
  template_url = models.FileField(upload_to="plantilla/upload/", max_length=100)

  def __str__(self):
    return self.template_name