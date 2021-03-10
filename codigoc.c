//se incluye la libreria a usar, en este caso fue wiringPi
//esta libreria ya venia instalada, sin embargo se puede instalar:
//sudo apt-get install git-core
//git clone git://git.drogon.net/wiringPi

#include <wiringPi.h>
int main(void)
{	
	//inicializa la configuracion de wiringPi
	wiringPiSetup();
	//se pone el pin 17del GPIO que corresponde con el 0 de wiringPi como salida
	pinMode(0, OUTPUT);
	//se crea el bucle de subida y bajada del pin del GPIO
	while(1)
	{
	//se levanta el pin 17 del GPIO 
	digitalWrite(0, HIGH);
	//se baja el pin 17 del GPIO
	digitalWrite(0, LOW);
	}
return 0;
}
