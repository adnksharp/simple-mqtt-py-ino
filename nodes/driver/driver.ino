#include "mosquitto.h"

#define LEDX 2
#define POT1 34
#define POT2 35
char* topic1 = "robot/velocidad/izquierda";
char* topic2 = "robot/velocidad/derecha";

struct Pot
{
	byte pin;
	char* topic;
};

MQTT mqtt;
Pot pot1;
Pot pot2;

void setup()
{
	mqtt.led = LEDX;
	pinMode(mqtt.led, OUTPUT);
	Serial.begin(115200);

	pot1.pin = POT1;
	pot1.topic = topic1;
	pot2.pin = POT2;
	pot2.topic = topic2;
	
	mqtt.init();
	digitalWrite(mqtt.led, LOW);
}

void loop()
{
	mqtt.verify();
	mqtt.exec();
	mqtt.publish(pot1.topic, pot1.pin);
	mqtt.publish(pot2.topic, pot2.pin);
	delay(25);
}
