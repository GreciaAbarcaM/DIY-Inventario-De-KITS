#!/usr/bin/python
#Ejemplo de Prueba para el LCD



import time
import Adafruit_CharLCD as LCD #Libreria importada Copyright (c) 2014 Adafruit Industries

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

#Iniciamos declarando valores
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows)


# Mostramos mensaje de dos lineas
lcd.clear()
lcd.message('Bienvenidx\nsi funciona')

# Esperamos 2 seg.
time.sleep(3.0)

# Demo showing the cursor.
lcd.clear()
lcd.show_cursor(True)
lcd.message('Si ves esto\nsigue el DIY')
lcd.show_cursor(True)
lcd.blink(True)
time.sleep(5.0)

# Stop blinking and showing cursor.
lcd.show_cursor(False)
lcd.blink(False)

# Demo scrolling message right/left.
lcd.clear()
message = 'Gracias'
lcd.message(message)
for i in range(lcd_columns-len(message)):
    time.sleep(0.5)
    lcd.move_right()
for i in range(lcd_columns-len(message)):
    time.sleep(0.5)
    lcd.move_left()

# Change message.
lcd.clear()
lcd.message('Adieu')

lcd.clear()
