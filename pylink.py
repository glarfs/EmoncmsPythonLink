import serial, sys
import httplib

conn = httplib.HTTPConnection("localhost")
ser = serial.Serial('/dev/ttyUSB0', 9600)

while 1:
	sys.stdout.write(ser.readline())	
	conn.request("GET", "/emoncms3/api/post?apikey=xxxxxxxxxxxxxxxxxxxxxxxxxxx&json="+ser.readline())
	response = conn.getresponse()
