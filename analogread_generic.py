#######################################################
# Heading: analogread.py
# Author: credit to Numato sample code
# Description: dev: /dev/ttyACM3, channel: 0
# Usage: just run this file with portName and channel
######################################################


import serial
import threading
import sys

portName = sys.argv[1]
channel = sys.argv[2]

def refresh():
  
    serPort = serial.Serial(portName,19200,timeout=1)
    serPort.write("adc read "+ str(channel) + "\r")
    response = serPort.read(25)
    print response[10:-3]

    threading.Timer(1.00,refresh()).start()
    serPort.close()

refresh()
