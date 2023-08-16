
from datetime import datetime
import Adafruit_CharLCD as LCD #Libreria importada Copyright (c) 2014 Adafruit Industries
import time


fechaAct = datetime.now()
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
                           
                           
lcd.message('Prestado')
lcd.clear()
time.sleep(2.0)
print(fechaAct)

