from flask import Flask, render_template
from Adafruit_BMP085 import BMP085
import datetime
import sys
import Adafruit_DHT
#From this
import RPi.GPIO as GPIO, time, os
DEBUG = 1;
GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.IN)
GPIO.setup(22,GPIO.IN)
GPIO.setup(10,GPIO.IN)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(9,GPIO.OUT)
def rctime (RCpin):
    reading = 0;
    GPIO.setup(RCpin,GPIO.OUT)
    GPIO.output(RCpin,GPIO.LOW)
    time.sleep(0.1)
    GPIO.setup(RCpin,GPIO.IN)
    while(GPIO.input(RCpin) == GPIO.LOW):
        reading+=1
    return reading
#upto this



bmp = BMP085(0x77)

app = Flask(__name__)

@app.route('/SENS.csv',methods=['GET','POST'])
def textf():
	error = None
	##ef read_process():
	#	myfile2 = open("SENS.txt","r")
	#	lines = myfile2.readline();
	#	for proc, line in lines:
	#		yield line
	#return Response(read_process(),mimetype='text/plain')
	#strg = "I will do something here"
	myfile = open("SENS.csv","r")
	strg = myfile.read()
	myfile.close()
	#response = make_response(csv)
	#response.header["Content-Disposition"]= "attachment;filename=sens.csv"
	return strg
	#return strg
@app.route("/r4on",methods=['GET','POST'])
def hello4():
	GPIO.output(9,GPIO.HIGH)
	return "relay 4 turned on"
@app.route("/r4off",methods=['GET','POST'])
def hello5():
	GPIO.output(9,GPIO.LOW)	
	return "relay 4 turned off"

@app.route("/r3on",methods=['GET','POST'])
def hello6():
	GPIO.output(11,GPIO.HIGH)
	return "relay 3 turned on"
@app.route("/r3off",methods=['GET','POST'])
def hello7():
	GPIO.output(11,GPIO.LOW)	
	return "relay 3 turned off"

@app.route("/r2on",methods=['GET','POST'])
def hello21():
	GPIO.output(5,GPIO.HIGH)
	return "relay 2 turned on"
@app.route("/r2off",methods=['GET','POST'])
def hello22():
	GPIO.output(5,GPIO.LOW)	
	return "relay 2 turned off"

@app.route("/r1on",methods=['GET','POST'])
def hello2():
	GPIO.output(6,GPIO.HIGH)
	return "relay 1 turned on"
@app.route("/r1off",methods=['GET','POST'])
def hello3():
	GPIO.output(6,GPIO.LOW)	
	return "relay 1 turned off"

@app.route("/")
def hello():
    tempr = "%.2f c" % bmp.readTemperature()
    pressure = "%.2f hPa" %bmp.readPressure()
    altitude = "%.2f m" %bmp.readAltitude()
    #hum, tem = Adafruit_DHT.read(11,9)
    #if hum == 'NONE':
    if(GPIO.input(27) == GPIO.LOW) and (GPIO.input(22) == GPIO.LOW) and (GPIO.input(10) == GPIO.LOW):
        gas = 20
    if(GPIO.input(27) == GPIO.LOW) and (GPIO.input(22) == GPIO.LOW) and (GPIO.input(10) == GPIO.HIGH):
        gas = 30
    if(GPIO.input(27) == GPIO.LOW) and (GPIO.input(22) == GPIO.HIGH) and (GPIO.input(10) == GPIO.LOW):
        gas = 40
    if(GPIO.input(27) == GPIO.LOW) and (GPIO.input(22) == GPIO.HIGH) and (GPIO.input(10) == GPIO.HIGH):
        gas = 50
    if(GPIO.input(27) == GPIO.HIGH) and (GPIO.input(22) == GPIO.LOW) and (GPIO.input(10) == GPIO.LOW):
        gas = 60
    if(GPIO.input(27) == GPIO.HIGH) and (GPIO.input(22) == GPIO.LOW) and (GPIO.input(10) == GPIO.HIGH):
        gas = 70
    if(GPIO.input(27) == GPIO.HIGH) and (GPIO.input(22) == GPIO.HIGH) and (GPIO.input(10) == GPIO.LOW):
        gas = 80
    if(GPIO.input(27) == GPIO.HIGH) and (GPIO.input(22) == GPIO.HIGH) and (GPIO.input(10) == GPIO.HIGH):
        gas = 90
    hum = gas;
    lgt = rctime(4)
    if lgt > 2500:
        lgt = 'Low'
    if 500 < lgt < 2500:
        lgt = 'Medium'
    if lgt < 500:
        lgt = 'High'
    now = datetime.datetime.now()
    timeString = now.strftime("%d-%m-%Y %H:%M")
    text_file = open("SENS.txt","a")
    text_file.write(timeString + str(tempr) + str(pressure) + str(altitude) + str(hum) + lgt + '\n')
    text_file.write("\r")
    text_file.close()
    csvfile = open("SENS.csv","a")
    csvfile.write(timeString + ',' + str(tempr) + ',' + str(pressure) + ',' + str(altitude) + ',' + str(hum) + ',' + lgt + '\n')
    csvfile.close()
    templateData = {
        'title' : 'HELLO!',
        'time' : timeString,
        'temp' :tempr,
        'pres' :pressure,
        'alt' : altitude,
        'humidity' : hum,
        'intens' : lgt
        }
    return render_template('main2.html',**templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
    
