#!/usr/bin/python
#Este código sirve para comprpbar si nos hemos conectado exitosamente a nuestra base de datos

import mysql
from mysql.connector import Error

try:
	conexion = mysql.connector.connect(
		host='localhost',
		user='kitsadmin',
		password='nuevaidea',
		db='registrokitsiot',
		port=3306
		)
		
	if conexion.is_connected():
		print("Conexión exitosa")
	
except Error as ex:
	print("Error de conexión:",ex)
	






finally:
	lcd.clear()
	if conexion.is_connected():
		conexion.close()
		lcd.message('Conexión Finalizada')
