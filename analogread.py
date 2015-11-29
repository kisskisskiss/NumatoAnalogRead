#######################################################
# Heading: analogread.py
# Author: credit to Numato sample code
# Description: dev: /dev/ttyACM3, channel: 0
# Usage: just run this file
######################################################


import serial
import threading

def refresh():
  
    serPort = serial.Serial("/dev/ttyACM3",19200,timeout=1)
    serPort.write("adc read 0" + "\r")
    response = serPort.read(25)
    print response[10:-3]

    threading.Timer(1.00,refresh()).start()
    serPort.close()

refresh()
