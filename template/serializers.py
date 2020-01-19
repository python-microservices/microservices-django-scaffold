from rest_framework import serializers

from template.models import Color


class ColorModelSerializer(serializers.ModelSerializer):
    """
    Example with a ModelSerializer
    """

    class Meta:
        model = Color
        fields = ('idpublic', 'name', 'timestamp')


class ColorSerializer(serializers.Serializer):
    """
    Example with a Serializer
    """
    idpublic = serializers.CharField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False, max_length=100)
    timestamp = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        """
        Create and return a new `Color` instance, given the validated data.
        """
        return Color.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Color` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
