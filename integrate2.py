import serial
import time
arduino_port = serial.Serial('/dev/ttyACM0', 9600)
baud_rate=9600
time.sleep(2)
def send_command(command):
	arduino_port.write(command.encode())
	time.sleep(0.1)
	
try:
	while True:
		command=input("Enter command('f','b','l','r','s','v<speed>'):")
		send_command(command)
		response= arduino_port.readline().decode().strip()
		print("Response:",response)
except KeyboardInterrupt:
	print("program stopped")

