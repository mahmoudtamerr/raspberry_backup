import serial
import time

# Establish the serial connection
arduino_port = serial.Serial('/dev/ttyACM0', 9600)
baud_rate = 9600
time.sleep(2)  # Wait for the connection to establish

def send_command(command):
    arduino_port.write(command.encode())  # Send command to Arduino
    time.sleep(0.1)  # Small delay for Arduino to process

def read_response():
    # Read the response from Arduino
    if arduino_port.in_waiting > 0:  # Check if data is available to read
        response = arduino_port.readline().decode().strip()
        return response
    return None

try:
    while True:
        command = input("Enter command ('f', 'b', 'l', 'r', 's', 'v<speed>'): ")
        send_command(command)
        time.sleep(0.5)  # Give Arduino time to respond
        
        response = read_response()
        if response:
            print("Response:", response)
        else:
            print("No response from Arduino.")
except KeyboardInterrupt:
    print("Program stopped.")
    arduino_port.close()  # Close the serial connection properly
