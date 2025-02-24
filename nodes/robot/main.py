from paho.mqtt import client
from numpy import cos, sin, array, dot
from tabulate import tabulate
import json

def calc(client, userdata, msg):
    topic = str(msg.topic)
    data = json.loads(msg.payload.decode('utf-8'))
    print(topic, data)

class MQTT():
    def __init__(self, version, broker = 'localhost', port = 8080, ka = 60):
        self.clients: list = []
        self.publish: list = []
        self.qos = 0
        
        self.host = client.Client(version)
        self.host.on_message = calc
        self.host.connect(str(broker), int(port), int(ka))

    def config(self, topic = None, sub = True):
        if not topic:
            return
        if sub:
            self.clients.append(topic)
            self.host.subscribe(str(topic), qos = self.qos)
            self.qos += 1

        else:
            self.publish.append(None)
            self.publish[-1] = str(topic)

    def exec(self):
        self.host.loop_forever()

if __name__ == '__main__':
    mqttver = client.CallbackAPIVersion.VERSION2
    mosquitto = MQTT(version = mqttver, broker = 'localhost', port = 1883, ka = 60)
    mosquitto.config(sub = True, topic = 'robot/velocidad/izquierda')
    mosquitto.config(sub = True, topic = 'robot/velocidad/derecha')
    mosquitto.config(sub = False, topic = 'robot/posicion')
    try:
        mosquitto.exec()
    except:
        pass
