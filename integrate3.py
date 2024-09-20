import serial
import time
arduino_port = 'usb-Arduino__www.arduino.cc__0043_A4830363835351C0D002-if00'
baud_rate=9600
time.sleep(2)
def send_command(command):
	arduino.write(command.encode())
	time.sleep(0.1)
	response= arduinp.readline().decode().strip()
	print("Response:",response)
try:
	while True:
		command=input("Enter command('f','b','l','r','s','v<speed>'):")
		if command.startswith('v'):
			speed=command.split()[1]
			send_command(f'v{speed}\n')
		else:
			send_command(command+'\n')
	except KeyboardInterrupt:
		print("program stopped")
finally:
arduino.close()
