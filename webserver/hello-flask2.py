from flask import Flask
from Adafruit_BMP085 import BMP085
import time

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the BMP085 and use STANDARD mode (default value)
# bmp = BMP085(0x77, debug=True)

bmp = BMP085(0x77)


app = Flask(__name__)
@app.route("/")
def hello():
    temp = bmp.readTemperature()
    pressure = bmp.readPressure()
    altitude = bmp.readAltitude()
  #  return "Hello World"
    
    return "Temperature: %.2f C" % temp
    return "Pressure:    %.2f hPa" % (pressure / 100.0)
    return "Altitude:    %.2f" % altitude
    


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80,debug=True)
