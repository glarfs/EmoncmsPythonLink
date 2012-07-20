import serial
import httplib

conn = httplib.HTTPConnection("localhost")
ser = serial.Serial('/dev/ttyUSB0', 9600)

while 1:
	conn.request("GET", "/emoncms3/api/post?apikey=xxxxxxxxxxxxxxxxxxxxxxxxxxx&json="+ser.readline())
