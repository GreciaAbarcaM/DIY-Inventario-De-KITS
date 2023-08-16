#!/usr/bin/python
#Este código sirve para grabar los tags RFID

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time
import Adafruit_CharLCD as LCD #Libreria importada Copyright (c) 2014 Adafruit Industries


reader = SimpleMFRC522()

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
	lcd.clear()#Limpiamos display
	lcd.message('Ingresa\n(N°KIT,ID,NOMBRE)')#Pedimos al usuario que ingrese sus datos separados por ,
	time.sleep(5.0)
	lcd.clear()
	datos= input()
	lcd.clear()
	lcd.message('Escanea\nLlavero RFID')
	time.sleep(5.0)
	reader.write(datos)
	lcd.clear()
	lcd.message('Grabado')


finally:
	GPIO.cleanup()


