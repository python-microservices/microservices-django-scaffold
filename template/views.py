from django.http import Http404
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from template.models import Color
from template.serializers import ColorSerializer, ColorModelSerializer


class ColorList(APIView):
    """
    Example of a APIView
    """

    def get(self, request, format=None):
        colors = Color.objects.all()
        serializer = ColorSerializer(colors, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ColorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ColorDetail(APIView):
    """
    Retrieve, update or delete a color instance.
    """

    def get_object(self, pk):
        try:
            return Color.objects.get(idpublic=pk)
        except Color.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        color = self.get_object(pk)
        serializer = ColorSerializer(color)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        color = self.get_object(pk)
        serializer = ColorSerializer(color, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        color = self.get_object(pk)
        color.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ExampleView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)


# ViewSets define the view behavior.
class ColorViewSet(viewsets.ModelViewSet):
    """
    Example of a ModelViewSet
    """
    lookup_field = 'idpublic'
    queryset = Color.objects.all()
    serializer_class = ColorModelSerializer
