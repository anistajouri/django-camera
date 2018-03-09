from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

#from webapi.Utils.Light import LightUp
#from webapi.serializers.MailPictureManagerSerializer import MailPictureManagerSerializer
import RPi.GPIO as GPIO


class  LightUp(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(19,GPIO.OUT)

        GPIO.output(19, GPIO.LOW)

        content = {'mail_address': 'anis.tajouri@gmail.com'}
        return Response(content)



class  LightDown(APIView):
    permission_classes = (AllowAny,)


    def get(self, request):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(19,GPIO.OUT)

        GPIO.output(19, GPIO.HIGH)
        content = {'mail_address': 'anis.tajouri@gmail.com'}
        return Response(content)
