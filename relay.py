import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(19,GPIO.OUT)
GPIO.output(19, GPIO.LOW)

raw_input("Press enter to continue...")

GPIO.output(19, GPIO.HIGH)
