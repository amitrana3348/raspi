import serial
ser = serial.Serial('/dev/ttyAMA0',9600)
ser.write("hello")
while True:
    data=ser.read()
    print "received from Lappy:" + data
