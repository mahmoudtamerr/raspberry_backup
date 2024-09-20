import serial
import time
#ser = serial.Serial('/dev/ttyACM0',9600)
arduino_port = 'usb-Arduino__www.arduino.cc__0043_A4830363835351C0D002-if00'
baud_rate = 9600
time.sleep(2)
while True:
    command=input("Enter command(f/b/l/r/s/v <speed>):")
    if command.lower() in ['f','b','l','r','s']:
        ser.write(command)
        if command.lower()!='s':
            speed=input("Enter speed(0-255):")
            ser.write(speed.encode())
        elif command.lower() == 'v':
            speed= input("Enter speed(0-255):")
            ser.write(command)
            ser.write(speed)
        else:
            print("Invalid command.")
        time.sleep(1)
