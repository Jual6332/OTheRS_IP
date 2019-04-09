#!/usr/bin/env python3
################################################################################
################################################################################
### Locate tiles - "serial.py" #################################################
################################################################################
##  Justin A, Pierre G.     ####################################################
##  OTheRS IP Lead          ####################################################
##  Date Created: 4/3/19    ####################################################
##  Date Modified: 4/7/19   ####################################################
################################################################################
# Main Purpose: Send control decisions
#####################---------Libraries---------################################
import serial
import time
#####################---------Main Code---------################################
ser = serial.Serial(timeout=1,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS)
ser.baudrate = 9600
ser.port = '/dev/ttyS0'
time.sleep(1)
ser.open()
print(ser.isOpen())

filename = "Outputs/temperatures_output.txt"
data = []
with open(filename, "r") as f:
	row = 0
	for line in f.read().strip().split("\n"):
		try:
			numbers = [float(i) for i in line.strip().split(" ")]
			#print(numbers)
			data.append(numbers)
		except Exception as e:
			print("Exception: {}".format(e))

while(1):
	try:
		ser.write("begin".encode("ascii"))
		for row in data:
			for col in row:
				tempz=col
				if tempz>=0:
					temp="0 "+str(tempz)+"\n"
					print(temp)
					ser.write(temp.encode('ascii'))
				else:
					temp="1 "+str(tempz)+"\n"
					ser.write(temp.encode('ascii'))
		ser.write("end".encode("ascii"))
		break;
		if ser.inWaiting() > 0:
				rec_data = ser.readline()
				new = rec_data.decode('utf-8')
				print(str(new) + ' - ')
				ser.write(rec_data)
		time.sleep(0.01)
	except Exception as e:
		print(e)
#####################-----------Close-----------################################
