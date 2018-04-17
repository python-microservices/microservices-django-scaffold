from rest_framework import serializers

from template.models import Color


# Serializers define the API representation.
class ColorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Color
        fields = ('id', 'name', 'timestamp')
