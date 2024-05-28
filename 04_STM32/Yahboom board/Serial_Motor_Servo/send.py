import serial
import time

port = serial.Serial('COM7', 115200, timeout=1)
if port.is_open:
    print('open')

    while True:
        data = input('data:')

        port.write(data.encode())

        resp = port.readline().decode().strip()
        if resp:
            print('response:', resp)

        time.sleep(1)

port.close()
