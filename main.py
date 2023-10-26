import asyncio
import time
import socket
from consts import *

# motor1 = Motor(pin_a=2, pin_b=4, enable_pin=5)
# motor2 = Motor(pin_a=13, pin_b=12, enable_pin=14)


async def read_socket_data(soc: socket.socket):
    print_loop = asyncio.get_event_loop()
    print_loop.create_task(async_print())
    while True:
        try:
            event = soc.recv(1024)
            print(event.decode())
            if event == MOTOR_ON_EVENT:
                print(event)
                print("movubg ig")
                # await motor1.set_pwm_frequency(40000)
                # await motor1.set_speed_in_percentage(100)
                # await motor2.set_pwm_frequency(40000)
                # await motor2.set_speed_in_percentage(100)
            elif event == MOTOR_OFF_EVENT:
                print(event)
                # await motor1.set_pwm_frequency(0)
                # await motor1.set_speed_in_percentage(0)
                # await motor2.set_pwm_frequency(0)
                # await motor2.set_speed_in_percentage(0)
                # await motor1.stop()
                # await motor2.stop()
            elif event == MOTOR_FORWARD_EVENT:
                print(event)
                # await motor1.move_forward()
                # await motor2.move_forward()
            elif event == MOTOR_BACKWARD_EVENT:
                print(event)
                # await motor1.move_backward()
                # await motor2.move_backward()
            time.sleep(1)
            soc.send(bytes("heollo", "utf8"))
        except Exception as e:
            print(e)
            break
        await asyncio.sleep(0.1)


async def async_print():
    while True:
        print("VROOM VROOM")
        time.sleep(5)


async def for_esp(host="192.168.0.114", port=42069):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    import network

    sta_if = network.WLAN(network.STA_IF)
    # while True:
    if not sta_if.isconnected():
        while not sta_if.isconnected():
            print("Connecting... not connected")
            time.sleep(2)
    try:
        sock.connect((host, port))
        await read_socket_data(soc=sock)
    except:
        print("nothing")


async def for_machine(host="192.168.0.114", port=42069):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    await read_socket_data(soc=sock)


if __name__ == "__main__":
    # asyncio.run(for_esp())
    asyncio.run(for_machine())
    # Start the asynchronous print loop
