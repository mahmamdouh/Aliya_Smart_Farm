import time
import serial

ser = serial.Serial(
port='/dev/ttyusb0,
baudrate = 2400,
parity=serial.PARITY_EVEN,
stopbits=serial.STOPBITS_ONE,
bytesize=serial.SEVENBITS,
timeout=None
)

while 1:
	x=ser.readline()
	print(x)