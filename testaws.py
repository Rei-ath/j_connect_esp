import utime
from machine import Pin, SPI
import network
import json
import random
import time
# from mpython import *
from machine import Timer
from umqtt.simple import MQTTClient

# Certificate path
cert_file = 'j-connect-thingy.cert.pem'
key_file = 'j-connect-thingy.private.key'

"""
Add your AWS resource information
"""

client_id = b'j-connect-thingy'
server = b'a2r4euk7l75oz1-ats.iot.eu-north-1.amazonaws.com'

def sub_cb(topic, msg, retained, duplicate):
    
    print((topic, msg, retained, duplicate))




def main():
    # try:
        with open(key_file, mode="rb") as f:
                key = f.read()
                # print(key.decode("utf-8"))
        with open(cert_file, mode="rb") as f:
                cert = f.read()
        client = MQTTClient(client_id, server, port=1883, ssl_params={"key": key, "cert": cert}, ssl=True)
        print(f"connecting to {client_id} on {server}")
        client.connect()
        client.setcallback(sub_cb)
        
        client.subscribe(topic=b'$aws/things/j-connect-thingy/shadow/get/accepted')
        while True:
            if True:
                client.check_msg()
                # Blocking wait for message
                client.wait_msg()
                print('time')
                time.sleep(1)
            else:
                # Non-blocking wait for message
                
                # Then need to sleep to avoid 100% CPU usage (in a real
                # app other useful actions would be performed instead)
                

if __name__ == "__main__":
    main()

