#!/usr/bin/env python3
################################################################################
################################################################################
### Locate tiles - "serial.py" #################################################
################################################################################
##  Justin A, Pierre G.     ####################################################
##  OTheRS IP Lead          ####################################################
##  Date Created: 4/3/19    ####################################################
##  Date Modified: 4/14/19  ####################################################
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

start = time.time()
filename = "Outputs/temperatures_output.txt"
data = []
with open(filename, "r") as f:
	row = 0
	for line in f.read().strip().split("\n"):
		try:
			numbers = [float(i) for i in line.strip().split(" ")]
			print(numbers)
			data.append(numbers)
		except Exception as e:
			print("Exception: {}".format(e))

while(1):
	try:
		ser.write("begin\n".encode("ascii"))
		for row in data:
			for col in row:
				tempz=col
				temp=""
				if tempz > 50.0:
					temp+="2 "
				elif tempz < -20.0:
					temp+="1 "
				else:
					temp+="0 "
				if tempz>=0:
					temp+="0 "+str(abs(tempz))+"\n"
					#print(temp)
					ser.write(temp.encode('ascii'))
				else:
					temp+="1 "+str(abs(tempz))+"\n"
					#print(temp)
					ser.write(temp.encode('ascii'))
		ser.write("end\n".encode("ascii"))
		break;
		if ser.inWaiting() > 0:
				rec_data = ser.readline()
				new = rec_data.decode('utf-8')
				print(str(new) + ' - ')
				ser.write(rec_data)
		time.sleep(0.01)
	except Exception as e:
		print(e)

end = time.time()
print("Timing Analysis: "+str(end-start)+" s")
#####################-----------Close-----------################################
