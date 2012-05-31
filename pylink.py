import serial
import httplib

conn = httplib.HTTPConnection("localhost")
ser = serial.Serial('/dev/ttyUSB3', 9600)

while 1:
	conn.request("GET", "/emoncms3/api/post?apikey=85b2e74c6ce93f50dbef8c7e099f1548&json="+ser.readline())
