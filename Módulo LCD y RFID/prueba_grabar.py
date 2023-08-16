#!/usr/bin/python
#Ejemplo de Prueba para leer RFID

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
	text= input('Datos Nuevos')
	print("Escanea tu\nllavero RFID")
	reader.write(text)
	print("LISTO!")


finally:
	GPIO.cleanup()
