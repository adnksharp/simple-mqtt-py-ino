# Plot the position of a robotic vacuum cleaner based on the robot's wheel velocities with MQTT

| ![](fig/graph.svg) | ![](https://upload.wikimedia.org/wikipedia/commons/7/76/Iclebo_smart_bottom.jpg) |
|---|---|

Graficando la posición de un robot tipo aspiradora en base a las velocidades de las ruedas del robot con MQTT y ESP32.

## Consideraciones a tener en cuenta

* En necesario conectar todos los nodos a la misma red WiFi.
* Las modulos de ESP32 no pueden conectarse a redes con seguridad WPA empresarial.

## Conexión de MQTT

### Broker con mosquitto

En caso de usar mosquitto, crear un broker con la configuración [mosquitto.conf](mqtt/mosquitto.conf):

```shell
mosquitto -v -c mqtt/mosquitto.conf
```

### Conexión con MQTTX (opcional)

| ![](https://i.imgur.com/9lMw0ot.png) | ![](https://i.imgur.com/zqvRTJp.png) |
|---|---|

1. Crear una conexión al `localhost`.
2. Crear una subscripción al topico `robot/#` dentro de la conexión creada o 
    
    1. Crear una suscripción al topico `robot/velocidad/izquierda`.
    2. Crear una suscripción al topico `robot/velocidad/derecha`.
    3. Crear una suscripción al topico `robot/posicion`. 

## Configuración de los nodos

### Nodo driver

#### 1

Es necesario crear un archivo `nodes/driver/wificonfig.h` con la siguiente estructura:

```c
const char* ssid = "SSID-WIFI";
const char* pass = "CONTRASEÑA-WIFI";
const char* host = "MQTT-BROKER";
const short port = 1883;
```

las constantes `host` y `port` corresponden a las direcciones ip y el puerto del equipo donde se esta ejecutando mosquitto.

#### 2

Modificar las definiciones `POT1`, `POT2` en `nodes/driver/driver.ino` con los pines a usar para cada potenciometro
