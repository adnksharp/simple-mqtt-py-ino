#include <WiFi.h>
#include <PubSubClient.h>
#include <ArduinoJson.h>

#if __has_include("wificonfig.h")
    #include "wificonfig.h"
#else
	const char* ssid = "SSID";
	const char* pass = "PASSWORD";
	const char* host = "10.42.0.1";
	const char* port = 1883;
#endif


WiFiClient web;
PubSubClient client(web);

struct MQTT
{
	int led;

	void init()
	{
		WiFi.begin(ssid, pass);
		while(WiFi.status() != WL_CONNECTED)
		{
			digitalWrite(led, !digitalRead(led));
			delay(50);
		}
		client.setServer(host, port);
	}

	void verify()
	{
		while(!client.connected())
		{
			if(client.connect("driver"))
				digitalWrite(led, LOW);
			else
			{
				delay(500);
				digitalWrite(led, !digitalRead(led));
			}
		}
	}

	void exec()
	{
		client.loop();
	}

	String jsonize(int pin)
	{
		JsonDocument json;
		json["read"] = analogRead(pin);
		json["time"] = millis();

		String msg;
		serializeJson(json, msg);
		return msg;
	}

	void publish(char* topic, byte pin)
	{
		client.publish(topic, jsonize(pin).c_str());
	}
};
