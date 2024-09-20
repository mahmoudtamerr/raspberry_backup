import gps
import time
from datetime import datetime
import ssl
from paho.mqtt import client as mqttc
from paho import mqtt
import json 
from pyPS4Controller.controller import Controller
import serial
arduino_port = serial.Serial('/dev/ttyACM0', 9600)
session = gps.gps(mode=gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
time.sleep(1)
def send_command(command):
	arduino_port.write(command.encode())
class MyController(Controller):
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

	#move the robot forward
    def on_up_arrow_press(self):
        command="f"
        send_command(command)
		
	#stop the robot	
    def on_up_down_arrow_release(self):
        command="s"
        send_command(command)
        
	#move the robot backward
    def on_down_arrow_press(self):
        command="b"
        send_command(command)
        
	#move the robot right
    def on_right_arrow_press(self):
        command="r"
        send_command(command)
        
	#stop the robot
    def on_left_right_arrow_release(self):
        command="s"
        send_command(command)
        
	#move the robot left
    def on_left_arrow_press(self):
        command="l"
        send_command(command)
       
controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# you can start listening before controller is paired, as long as you pair it within the timeout window
controller.listen(timeout=60)
