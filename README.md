# embebidos-proyecto1
manejo de sensor 1-wire y conmutación de pin GPIO

el siguiente repositorio presenta scrips de  bash, c y python, que permiten la conmutación del pin 17 del GPIO de la raspberry.
Para la implementación de C, se utilizo la ligreria wiringPi y para la implementación de python, se utilizo RPi.GPIO, esto con el fin de poder acceder al GPIO de la tarjeta.
Para la implementación de los scripts no se empleo ningun tipo de sleep, dado a que se requeria que la velocidad de conmutación fuera la maxima  posible del sistema.
las implementaciones fueron las siguientes:

Bash  -----> https://github.com/nicolasego/embebidos-proyecto1/blob/main/bashpro.sh
C     -----> https://github.com/nicolasego/embebidos-proyecto1/blob/main/codigoc.c
python-----> https://github.com/nicolasego/embebidos-proyecto1/blob/main/python.py

Por otro lado, el repositorio cuenta con un script adicional, que fue utilizado para la  extracción de medida de temperatura del sensor DS18B20 que funciona con protocolo 1-wire.
En dicho script, se accede a la medida y se envia a un archivo CSV, en el encontramos una columna que presenta la fecha y hora de la extracción de la medida y una segunda columna que corresponde con la medidad de temperatura ajustada a dos cifras significativas despues de la coma.
la implementación se puede encontrar en:
https://github.com/nicolasego/embebidos-proyecto1/blob/main/temperatura.sh

