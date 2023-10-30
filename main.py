import uasyncio
import time
import socket
from consts import *
from motor import Motor

motor1 = Motor(pin_a=2, pin_b=4, enable_pin=5)
motor2 = Motor(pin_a=13, pin_b=12, enable_pin=14)
motor1.set_speed_in_percentage(100)


# motor2.set_pwm_frequency(40000)
motor2.set_speed_in_percentage(100)
async def vroom():
    while True:
        print("VROOOOOMMM...")
        await uasyncio.sleep(6)

async def read_socket_data(soc: socket.socket):
    # print_loop = uasyncio.get_event_loop()
    # print_loop.create_task(vroom())
    while True:
        try:
            data = soc.recv(10)
            # soc.send(bytes()"lol")
            # soc.send(b"lol")
            while not data:
                print("vroom")

            if len(data) == 1:
                print("data is ",data)
                print(len(data),"data lenght")
                event = int.from_bytes(data, 'big')
                print(data)
                if event == MOTOR_ON_EVENT:
                    print("Moving ig")
                    # await motor1.set_pwm_frequency(40000)
                    await motor1.set_speed_in_percentage(100)
                    # await motor2.set_pwm_frequency(40000)
                    await motor2.set_speed_in_percentage(100)
                elif event == MOTOR_OFF_EVENT:
                    print("Stopping motors")
                    await motor1.set_pwm_frequency(0)
                    await motor1.set_speed_in_percentage(0)
                    await motor2.set_pwm_frequency(0)
                    await motor2.set_speed_in_percentage(0)
                    await motor1.stop()
                    await motor2.stop()
                elif event == MOTOR_FORWARD_EVENT:
                    print("Moving forward")
                    await motor1.move_forward()
                    await motor2.move_forward()
                elif event == MOTOR_BACKWARD_EVENT:
                    print("Moving backward")
                    await motor1.move_backward()
                    await motor2.move_backward()
                elif event == MOTOR_RIGHT_EVENT:
                    print("Moving right")
                    await motor2.move_backward()
                    time.sleep(0.01)
                    await motor2.move_forward()
                elif event == MOTOR_LEFT_EVENT:
                    print("Moving left")
                    await motor1.move_backward()
                    time.sleep(0.01)
                    await motor1.move_forward()
            # soc.send(bytes("heollo", "utf-8"))
            print("Going to sleep for 1 second")
                
            await uasyncio.sleep(.4)
        except Exception as e:
            print(e)
            # break
        print("Going to sleep for 1 second")
        await uasyncio.sleep(0.1)

async def for_esp(host="192.168.0.110", port=42069):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    import network

    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        while not sta_if.isconnected():
            print("Connecting... not connected")
            await uasyncio.sleep(2)
    try:
        ip_address = sta_if.ifconfig()[0]
        print(f"connecting with {ip_address}")
        sock.connect((host, port))
        print(f"connected with {ip_address}")
        await read_socket_data(soc=sock)
        # asyncio.create_task (read_socket_data(sock))
        # asyncio.create_task(vroom())

    except Exception as e:
        print(e)
        print("nothing")

def for_machine(host="192.168.0.110", port=42069):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    print("connected")
    read_socket_data(sock)

if __name__ == "__main__":
    uasyncio.run(for_esp())
