import serial

port = serial.Serial('COM7', 115200, timeout=1)
if port.is_open:
    print('open')

    while True:
        data = port.readline().decode().strip()

        if data:
            print(data)

else:
    print('fail')

port.close()
