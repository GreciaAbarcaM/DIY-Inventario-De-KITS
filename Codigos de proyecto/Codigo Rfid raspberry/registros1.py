#!/usr/bin/env python
import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import mysql.connector
import Adafruit_CharLCD as LCD
import registrokitiot


db = mysql.connector.connect(
	host="localhost",
	user="kitsadmin",
	passwd="nuevaidea",
	database="registrokitsiot"
)
