#!/usr/bin/python
#Este código compila los módulos LCD y RC522 para generar un registro
#control de préstamos de KITs IOT


import datetime#import datetime; este es el paquete comleto, lo reducimos
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time
import Adafruit_CharLCD as LCD #Libreria importada Copyright (c) 2014 Adafruit Industries
import mysql.connector
from mysql.connector import Error


reader = SimpleMFRC522()

fechaAct = datetime.datetime.now()

#Configuramos los pines de la Raspberry Pi4
lcd_rs        = 4  #Puede que necesites cambiarlo por 21 en versiones anteriores de Pi.
lcd_en        = 24
lcd_d4        = 23
lcd_d5        = 17
lcd_d6        = 18
lcd_d7        = 22

#Definimos columnas y filas LCD 16x2
lcd_columns = 16
lcd_rows    = 2

#Iniciamos declarando LCD
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows)
                           

try:
	lcd.clear()
	lcd.message('Escanea\nLlavero RFID')
	time.sleep(2.0)
	id, text = reader.read()
	print(id)
	lcd.message('Listo!')
	lcd.clear()
	time.sleep(2.0)
	lcd.message('Prestado')
	time.sleep(2.0)
	print(fechaAct)
	


finally:
	GPIO.cleanup()



