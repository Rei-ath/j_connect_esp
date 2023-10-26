# This file is executed on every boot (including wake-boot from deepsleep)
import esp
esp.osdebug(None)
import time
import webrepl
webrepl.start()
def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(True)
    print(sta_if.isconnected())
    if not sta_if.isconnected():
        print('Connecting to network...')
        sta_if.active(True)
        print(sta_if.ifconfig())
        sta_if.connect('Om so f1', 'Guru@123')  # Replace with your WiFi credentials
        while not sta_if.isconnected():
            print("Connecting...")
            time.sleep(2)
    print('Network config:', sta_if.ifconfig())
do_connect()