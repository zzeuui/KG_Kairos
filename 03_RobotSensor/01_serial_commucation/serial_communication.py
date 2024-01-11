import serial
import time

ser = serial.Serial("COM3", 115200)

while True:
    if ser.inWaiting() > 0:
        data = ser.readline().decode()
        print(data, end='')

    ser.write('a'.encode())
    time.sleep(1)
    ser.write('b'.encode())
    time.sleep(1)

