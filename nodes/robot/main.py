from paho.mqtt import client
from numpy import cos, sin, array, dot
import tabulate.tabulate as tab

class MQTT():
    def __init__(self, broker = 'localhost', port, ka):
        topics: list = []
        clients: list = []
        publish: list = []
        self.broker = str(broker)
        self.port = int(port)
        self.ka = int(ka)
        self.quos = 0

    def config(self, version, sub = False, topic = None):
        self.clients.append(client(version))
        self.publish.append(None)

        self.clinets[-1].connect(self.broker, self.port, self.ka)
        if topic:
            if sub:
                self.clients[-1].subscribe(str(topic), quos = self.quos)
                self.quos += 1
            else:
                self.pusblish[-1] = str(topic)

    def exec(self):
        for client in self.clients:
            client.toop_forever()
