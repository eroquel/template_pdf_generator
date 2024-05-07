import base64
import json

from django.template.loader import get_template
from xhtml2pdf import pisa

from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.template import loader

from plantilla.models import Plantilla
from plantilla.serializer import PlantillasSerializer

class ListPlantillasAPIView(viewsets.ModelViewSet):
    queryset = Plantilla.objects.all()
    serializer_class = PlantillasSerializer

@api_view(["POST"])
def GeneratePDf(request):

    try:
        data = json.loads(request.body.decode("utf-8"))
        plantilla = Plantilla.objects.get(template_name=data["template_name"])
        template_url = plantilla.template_url
        templateFileName = str(template_url).split("/")[-1]

        template = get_template(templateFileName)
        html = template.render(data["context"])
        #print(data["context"])

        pdf_file = HttpResponse(content_type="application/pdf")
        pisa.CreatePDF(html, dest=pdf_file)
        pdf_content = pdf_file.content

        encoded_pdf = base64.b64encode(pdf_content).decode("utf-8")
        response_data = {"pdf": encoded_pdf}

        return Response(response_data, status=status.HTTP_200_OK)

    except Plantilla.DoesNotExist:
        error = {"status": status.HTTP_404_NOT_FOUND, "msg": "Plantilla no existe"}
        return Response(error, status=status.HTTP_404_NOT_FOUND)
