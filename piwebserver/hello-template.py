from flask import Flask, render_template
from Adafruit_BMP085 import BMP085
import datetime
import sys
#import Adafruit_DHT
#From this
import RPi.GPIO as GPIO, time, os
DEBUG = 1;
GPIO.setmode(GPIO.BCM)
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
@app.route("/")
def hello():
    tempr = "%.2f c" % bmp.readTemperature()
    pressure = "%.2f hPa" %bmp.readPressure()
    altitude = "%.2f m" %bmp.readAltitude()
   # hum, tem = Adafruit_DHT.read(11,9)
    #if hum == 'NONE':
    hum = 40;
    lgt = rctime(10)
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
    
