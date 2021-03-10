#!/bin/bash
#elimina el control del gpio en el espacio de usuario
echo "17" > /sys/class/gpio/unexport
#exporta el pin al espacio de usuario lo que permite que se use el pin
echo "17" > /sys/class/gpio/export
#se genera un sleep para que se alcance a ejecutar la subida y bajada
sleep 0.5
#se pone el pin 17 del GPIO como una salida
echo "out" > /sys/class/gpio/gpio17/direction
#se genera el bucle para subir y bajar el pin
while [ true ]
do
	#se levanta el pin 17 del GPIO
	echo "1" > /sys/class/gpio/gpio17/value
	#se baja el pin 17 del GPIO
	echo "0" > /sys/class/gpio/gpio17/value
done
