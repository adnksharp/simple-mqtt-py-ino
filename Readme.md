# Plot the position of a robotic vacuum cleaner based on the robot's wheel velocities with MQTT

| ![](fig/graph.svg) | ![](https://upload.wikimedia.org/wikipedia/commons/7/76/Iclebo_smart_bottom.jpg) |
|---|---|

Graficando la posición de un robot tipo aspiradora con base en las velocidades de las ruedas del robot con MQTT y ESP32.

## Consideraciones a tener en cuenta

* Es necesario conectar todos los nodos a la misma red WiFi.
* Los módulos de ESP32 no pueden conectarse a redes con seguridad WPA empresarial.

* Es necesario tener las siguientes librerías de Python:
    - paho-mqtt
    - matplotlib
    - json
    - numpy

    ```bash
    pip install -r requirements.txt
    ```

## Conexión de MQTT

### Broker con mosquitto

En caso de usar mosquitto, crea un broker con la configuración [mosquitto.conf](mqtt/mosquitto.conf):

```shell
mosquitto -v -c mqtt/mosquitto.conf
```

### Conexión con MQTTX (opcional)

| ![](https://i.imgur.com/9lMw0ot.png) | ![](https://i.imgur.com/zqvRTJp.png) |
|---|---|

1. Crear una conexión al `localhost`.
2. Generar una subscripción al topico `robot/#` dentro de la conexión hecha o, 
    
    1. Generar una suscripción al topico `robot/velocidad/izquierda`.
    2. Generar una suscripción al topico `robot/velocidad/derecha`.
    3. Generar una suscripción al topico `robot/posicion`. 

## Nodo driver

### 1

Es necesario crear un archivo `nodes/driver/wificonfig.h` con la siguiente estructura:

```c
const char* ssid = "SSID-WIFI";
const char* pass = "CONTRASEÑA-WIFI";
const char* host = "MQTT-BROKER";
const short port = 1883;
```

Las constantes `host` y `port` corresponden a las direcciones ip y el puerto del equipo donde se está ejecutando mosquitto.

### 2

Modificar las definiciones `POT1`, `POT2` en `nodes/driver/driver.ino` con los pines a usar para cada potenciometro

### 3

Cargar el sketch `nodes/driver` a una placa de desarrollo ESP32.

## Nodo robot

Para suscribirse a los tópicos `robot/velocidad/#`, procesar los datos y mandarlos al tópico `robot/posicion` ejecutar el script [robot](nodes/robot/main.py):

```shell
python nodes/robot/main.py
```

o 

```shell
python3 nodes/robot/main.py
```

## Nodo plot

El nodo plot se encarga de graficar los datos del tópico `robot/posicion`:

```shell
python nodes/plot/main.py
```

o 

```shell
python3 nodes/plot/main.py
```