from paho.mqtt import client
from numpy import cos, sin, array, dot
from tabulate import tabulate
import json

def calc(client, userdata, msg):
    topic = str(msg.topic)
    data = json.loads(msg.payload.decode('utf-8'))
    print(topic, data)

class MQTT():
    def __init__(self, broker = 'localhost', port = 8080, ka = 60):
        self.clients: list = []
        self.publish: list = []
        self.broker = str(broker)
        self.port = int(port)
        self.ka = int(ka)
        self.qos = 0

    def config(self, version, sub = False, topic = None):
        if not topic:
            return
        if sub:
            self.clients.append(client.Client(version))
            self.clients[-1].on_message = calc
            self.clients[-1].connect(self.broker, self.port, self.ka)
            self.clients[-1].subscribe(str(topic), qos = self.qos)
            self.qos += 1

        else:
            self.publish.append(None)
            self.publish[-1] = str(topic)

    def exec(self):
        for client in self.clients:
            client.loop_forever()

if __name__ == '__main__':
    mqttver = client.CallbackAPIVersion.VERSION2
    mosquitto = MQTT(broker = 'localhost', port = 1883, ka = 60)
    mosquitto.config(version = mqttver, sub = True, topic = 'robot/velocidad/izquierda')
    mosquitto.config(version = mqttver, sub = True, topic = 'robot/velocidad/derecha')
    mosquitto.config(version = mqttver, sub = False, topic = 'robot/posicion')
    try:
        mosquitto.exec()
    except:
        pass
