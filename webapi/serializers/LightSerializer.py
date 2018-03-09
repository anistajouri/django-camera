from rest_framework import serializers


class LightSerializer(serializers.Serializer):

    light = serializers.CharField(max_length=250)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
