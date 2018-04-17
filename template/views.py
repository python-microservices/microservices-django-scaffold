from rest_framework import viewsets

from template.models import Color
from template.serializers import ColorSerializer


# ViewSets define the view behavior.
class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
