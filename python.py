#primero importamos la libreria para usar el GPIO desde python que en este caso fue RPi.GPIO
#en caso de que no este instalada se puede instalar de la siguiente forma:
#sudo apt-get install python-dev
#sudo apt-get install pyton-rpi.gpio
import RPi.GPIO as GPIO
#se establece la numeración de la tarjeta
GPIO.setmode(GPIO.BOARD)
#se pone el pin 11 fisico de la tarjeta que corresponde con el 17 del GPIO como salida
GPIO.setup(11,GPIO.OUT)
#se crea el bucle para subir y bajar el pin del GPIO
while 1:
	#se pone en alto el pin 11
	GPIO.output(11, GPIO.HIGH)
	#se baja el pin 11
	GPIO.output(11, GPIO.LOW)
