from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from webapi.Utils.MailPictureManager import MailPictureManager
from webapi.serializers.MailPictureManagerSerializer import MailPictureManagerSerializer

class MailPictureManagement(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        """
        Get the mail_address
        """
        MailPictureManager.email_photo()       
#        content = {'mail_address': MailPictureManager.get_mail_address()}
        content = {'mail_address': 'anis.tajouri@gmail.com'}
        return Response(content)

    # def post(self, request):
    #     serializer = MailPictureManagerSerializer(data=request.data)

    #     if serializer.is_valid():
    #         MailPictureManager.set_picture_nbr(serializer.validated_data["mail_address"])
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
