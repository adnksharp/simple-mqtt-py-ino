from paho.mqtt import client
from numpy import cos, sin, array, dot
from tabulate import tabulate
import json

class Mathematize():
    def __init__(self, R = 0.02, L = 0.1):
        self.x, self.y, self.theta = 0.0, 0.0, 0.0
        self.data:list = [0.0, 0.0]
        self.R, self.L = R, L
        self.last = None

    def getVel(self):
        v = self.data
        T = array([
            [self.R/2 * cos(self.theta), self.R / 2 * cos(self.theta)],
            [self.R/2 * sin(self.theta), self.R / 2 * sin(self.theta)],
            [self.R/self.L , -self.R/self.L]
        ])

        return dot(T, v).tolist()

    def getPos(self, v, dt):
        vx, vy, vt = v

        return [self.x + vx * dt, self.y + vy * dt, self.theta + vt * dt]

    def index(self, topic, data):
        if topic == 'robot/velocidad/derecha':
            self.data[0] = data['read']
        elif topic == 'robot/velocidad/izquierda':
            self.data[1] = data['read']

    def getdt(self, millis):
        if self.last is None:
            self.last = millis
            return None
        dt = (millis - self.last) / 1000.0
        self.last = millis

        return dt

    def get(self, client, userdata, msg):
        topic = str(msg.topic)
        data = json.loads(msg.payload.decode('utf-8'))
        self.index(topic, data)
        dt = self.getdt(float(data['time']))
        if dt is None:
            return
        self.x, self.y, self.theta = self.getPos(self.getVel(), dt)
        print(tabulate([self.data, [self.x, self.y, self.theta]], floatfmt='.5f', tablefmt='simple_grid'))


class MQTT():
    def __init__(self, version, broker = 'localhost', port = 8080, ka = 60, f = None):
        self.clients: list = []
        self.publish: list = []
        self.qos = 0
        
        self.host = client.Client(version)
        self.host.on_message = f
        self.host.connect(str(broker), int(port), int(ka))

    def config(self, topic = None, sub = True):
        if not topic:
            return
        if sub:
            self.clients.append(topic)
            self.host.subscribe(str(topic), qos = self.qos)
            self.qos += 1

        else:
            self.publish.append(str(topic))

    def exec(self):
        try:
            self.host.loop_forever()
        except:
            pass


if __name__ == '__main__':
    mqttver = client.CallbackAPIVersion.VERSION2
    math = Mathematize(R = 0.5, L = 0.1)
    mosquitto = MQTT(version = mqttver, broker = 'localhost', port = 1883, ka = 60, f = math.get)
    mosquitto.config(sub = True, topic = 'robot/velocidad/izquierda')
    mosquitto.config(sub = True, topic = 'robot/velocidad/derecha')
    mosquitto.config(sub = False, topic = 'robot/posicion')
    mosquitto.exec()
