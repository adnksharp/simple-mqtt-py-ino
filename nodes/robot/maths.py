import json
from numpy import cos, sin, array, dot
from tabulate import tabulate

def tab(*prints):
    print(tabulate(prints, floatfmt='.5f', tablefmt='simple_grid'))

class Mathematize():
    def __init__(self, R = 0.02, L = 0.1, topic ='test'):
        self.x, self.y, self.theta = 0.0, 0.0, 0.0
        self.data:list = [0.0, 0.0]
        self.R, self.L = R, L
        self.last = None
        self.topic = topic

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
        tab(self.data, [self.x, self.y, self.theta])

        pub = '{' + '"pos":[{},{},{}]'.format(self.x, self.y, self.theta) + '}'
        client.publish(self.topic, f'{pub}')
