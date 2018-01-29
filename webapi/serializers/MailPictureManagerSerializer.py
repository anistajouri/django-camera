from rest_framework import serializers


class MailPictureManagerSerializer(serializers.Serializer):

    mailpicture = serializers.CharField(max_length=250)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
