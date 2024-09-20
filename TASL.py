import time 
import paho.mqtt.client as paho
from paho import mqtt
import serial
import time
from pyPS4Controller.controller import Controller
serial1 = serial.Serial('/dev/ttyACM0', 9600)
def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)

def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))

def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_message(client, userdata, msg):
    speed = msg.payload
    serial1.write(speed)

client = paho.Client(client_id="11558", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect

client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set("mahmoud", "12345678@Nu")
client.connect("b32caacf49864326847d6cbb1722c04c.s1.eu.hivemq.cloud", 8883)

client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_publish = on_publish
client.publish("location", payload=194, qos=1)
client.loop_forever()





