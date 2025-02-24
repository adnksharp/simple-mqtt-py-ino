#include "mosquitto.h"

struct Potenciometer
{
	byte pin;
	String topic;
};

MQTT mqtt;


void setup()
{
	mqtt.broker = "10.0.0.6";
	mqtt.port = 1883;
	mqtt.led = 2;
	pinMode(mqtt.led, OUTPUT);
	Serial.begin(115200);
	
	mqtt.init();
	digitalWrite(mqtt.led, LOW);
}

void loop()
{
	mqtt.verify();
	mqtt.exec();
	mqtt.publish("robot/velocidad/izquierda", 34);
	delay(2500);
}
