from mosquitto import MQTT, client
import json

def plot(client, userdata, msg):
    data = json.loads(msg.payload.decode('utf-8'))
    print(data['pos'])

if __name__ == '__main__':
    mqttver = client.CallbackAPIVersion.VERSION2
    mosquitto = MQTT(version = mqttver, broker = 'localhost', port = 1883, ka = 60, f = plot)
    mosquitto.config(topic = 'robot/posicion')
    mosquitto.exec()
