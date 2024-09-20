import requests
import RPi.GPIO as GPIO         # Import Raspberry Pi GPIO library
from time import sleep          # Import the sleep function 
url= 'http://192.168.137.1:3000'

pinLED = 17                     # LED GPIO Pin

GPIO.setmode(GPIO.BCM)          # Use GPIO pin number
GPIO.setwarnings(False)         # Ignore warnings in our case
GPIO.setup(pinLED, GPIO.OUT)    # GPIO pin as output pin

while True:                          # Endless Loop
    GPIO.output(pinLED, GPIO.HIGH)   # Turn on
    print('LED on')   
    myobj = {'LED' : 'ON'}
    x = requests.post(url, json = myobj)
    print(x.text)                 # Prints state to console
    sleep(30)                         # Pause 1 second
    GPIO.output(pinLED, GPIO.LOW)    # Turn off
    print('LED off') 
    myobj = {'LED' : 'OFF'}
    x = requests.post(url, json = myobj)
    print(x.text)                  # Prints state to console
    sleep(30)                         # Pause 1 second


