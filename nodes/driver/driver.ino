#include "mosquitto.h"
#define LEDX 2
#define POT1 34
#define POT2 35

struct Pot
{
	byte pin;
	String topic;
};

MQTT mqtt;
Pot pot1;
Pot pot2;

const String topics [] = {
	"robot/velocidad/izquierda",
	"robot/velocidad/derecha"
};

void setup()
{
	mqtt.led = LEDX;
	pinMode(mqtt.led, OUTPUT);
	Serial.begin(115200);

	pot1.pin = POT1;
	pot1.topic = topics[0];
	pot2.pin = POT2;
	pot2.topic = topics[1];
	
	mqtt.init();
	digitalWrite(mqtt.led, LOW);
}

void loop()
{
	mqtt.verify();
	mqtt.exec();
	mqtt.publish(pot1.topic, pot1.pin);
	mqtt.publish(pot2.topic, pot2.pin);
	delay(2500);
}
