import RPi.GPIO as GPIO
import time
import requests

# GPIO setup
LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# Node.js server URL
SERVER_URL = "http://<your_laptop_ip>:3000/status"

# Toggle LED and send status to server
def send_status(status):
    try:
        response = requests.post(SERVER_URL, json={"status": status})
        print(f"Sent {status} to server. Response: {response.status_code}")
    except Exception as e:
        print(f"Error sending status to server: {e}")

try:
    while True:
        # Turn LED on
        GPIO.output(LED_PIN, GPIO.HIGH)
        send_status("on")
        time.sleep(60)  # Keep LED on for 1 minute

        # Turn LED off
        GPIO.output(LED_PIN, GPIO.LOW)
        send_status("off")
        time.sleep(60)  # Keep LED off for 1 minute

except KeyboardInterrupt:
    print("Script stopped by user.")

finally:
    GPIO.cleanup()
