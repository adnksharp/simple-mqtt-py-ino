from maths import Mathematize
from mosquitto import MQTT, client

if __name__ == '__main__':
    mqttver = client.CallbackAPIVersion.VERSION2
    math = Mathematize(R = 0.5, L = 0.1, topic = 'robot/posicion')
    mosquitto = MQTT(version = mqttver, broker = 'localhost', port = 1883, ka = 60, f = math.get)
    mosquitto.config(topic = 'robot/velocidad/izquierda')
    mosquitto.config(topic = 'robot/velocidad/derecha')
    mosquitto.exec()
