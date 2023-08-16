#PRUEBA1 DE CODIGO PYTHON

import registrokitsiot
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import mysql.connector
import pymysql

connection = pymysql.connect()
	host="localhost",
	user="kitsadmin",
	passwd="nuevaidea",
	db="registrokitsiot"P
	)
	
cursor = connection.cursor()
reader = SimpleMFRC522()
lcd = LCD.Adafruit_CharLCD(4, 24, 23, 17, 18, 22, 16, 2)
sql = "INSERT INTO PruebaIN(id_kit, id_usuario, fecha, usuario) VALUES('', '', '', '')"

try:
	while True:
		lcd.clear()
		lcd.message('Escanea tu\nllavero RFID')
		id_kit, text = reader.read()
		cursor.execute("SELECT id_kit FROM PruebaIN WHERE id_usuario="+str(id_kit))
		cursor.fetchone()
		
		if cursor.rowcount >= 1;
			lcd.clear()
			lcd.message("Ingresa Usuario=")
			overwrite = input("Ingresar (Y/N)")
			if overwrite[0] == 'Y' or overwrite[0] == 'y':
				lcd.clear()
				lcd.message("Ingresa Usuario.")
				time.sleep(1)
				sql_insert ="UPDATE PruebaIN set usuario = %s WHERE id_usuario=%s"
			else:
				continue
		else:
			sql_inset = "INSERT INTO PruebaIN (usuario, id_usuario) VALUES (%S, %S)"
		lcd.clear()
		lcd.message('Ingresa nuevo\nnombre:')'   
		 new_name = input("Nombre:")
		 
		 cursor.execute(sql_insert, (new_name, id_kit))
		 connection.commit()
		 
		 lcd.clear()
		 lcd.message("Usuario " + new_name + "Guardado")
		 time.sleep(2)
finally:
	GPIO.cleanup()
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 



cursor.execute(sql)
connection.commit()
