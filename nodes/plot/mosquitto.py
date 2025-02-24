from paho.mqtt import client

class MQTT():
    def __init__(self, version, broker = 'localhost', port = 8080, ka = 60, f = None):
        self.qos = 0
        
        self.host = client.Client(version)
        self.host.on_message = f
        self.host.connect(str(broker), int(port), int(ka))

    def config(self, topic = None):
        if not topic:
            return
        self.host.subscribe(str(topic), qos = self.qos)

    def exec(self):
        try:
            self.host.loop_start()
        except:
            pass
