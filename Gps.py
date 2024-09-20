import gps
import time
from datetime import datetime
import ssl
from paho.mqtt import client as mqttc
from paho import mqtt
import json 
session = gps.gps(mode=gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)

def on_publish(client, userdata, mid, properties=None):
    pass
client = mqttc.Client(client_id="7553392", userdata=None, protocol=mqttc.MQTTv5)
client.on_connect = on_connect
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set("raspberry", "12345678@No")
client.connect("b32caacf49864326847d6cbb1722c04c.s1.eu.hivemq.cloud", 8883)
client.on_publish = on_publish
try:
    while True:
        try:
            report = session.next()
        except KeyError as e:
            print(f"Error reading GPS data: {e}")
        except StopIteration:
            print("No more GPS data or GPSD servicestopped.")
        except Exception as e:
            print(f"An unexpected error occured: {e}")
            break
        if report['class'] == 'TPV':
            
            latitude = getattr(report, 'lat', "Unknown")
            longitude = getattr(report, 'lon', "Unknown")
            time_utc = getattr(report, 'time', "Unknown")  
            serial = getattr(report, 'device', "Unknown")  
            
            gps_data = {
                "name": time_utc,
                "latitude": latitude,
                "longitude": longitude,
            }
            gps_data_json = json.dumps(gps_data)
            client.publish("location", payload= gps_data_json , qos=1 )
            print(f"Published to MQTT topic location: {gps_data}")
            client.loop()
            time.sleep(10)
except KeyboardInterrupt:
    # Exit the program gracefully if Ctrl+C is pressed
    print("GPS data collection stopped.")

except StopIteration:
    # Handle GPS signal loss or end of data stream
    print("GPSD has stopped.")
finally:
	client.disconnect()


