import serial, sys
ser = serial.Serial('/dev/ttyUSB0', 9600)
while 1 :
        sys.stdout.write(ser.readline())

