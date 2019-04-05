import serial
import time

ser = serial.Serial(timeout=1,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS)
ser.baudrate = 9600
ser.port = '/dev/ttyS0'
time.sleep(1)
ser.open()
print(ser.isOpen())
while(1):
	try:
		#temp = '0'
		#ser.write(temp.encode('ascii'))
		if ser.inWaiting() > 0:
			rec_data = ser.readline()
			new = rec_data.decode('utf-8')
			print(str(new) + ' - ')
			ser.write(rec_data)
		time.sleep(0.01)
	except Exception as e:
		print(e)
