from graph import Plot
from mosquitto import MQTT, client
import json

if __name__ == '__main__':
    mqttver = client.CallbackAPIVersion.VERSION2
    plot = Plot()
    mosquitto = MQTT(version = mqttver, broker = 'localhost', port = 1883, ka = 60, f = plot.get)
    mosquitto.config(topic = 'robot/posicion')
    mosquitto.exec()

    while True:
        try:
            plot.show()
        except KeyboardInterrupt:
            exit()
