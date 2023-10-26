from microdot_asyncio import Microdot, Response, send_file
from microdot_utemplate import render_template
from microdot_asyncio_websocket import with_websocket
import  asyncio
from motor import Motor
motor1 = Motor(pin_a=2, pin_b=4, enable_pin=5)
motor2 = Motor(pin_a=13, pin_b=12, enable_pin=14)

# from ldr_photoresistor_module import LDR
import time

# Initialize MicroDot
app = Microdot()
Response.default_content_type = 'text/html'

# LDR module


# # root route
# @app.route('/')
# async def index(request):
#     return render_template('index.html')

async def async_print():
    while True:
        print("VROOM VROOM")
        time.sleep(5)


@app.route('/')
@with_websocket
async def read_socket_data(request,ws):
    print_loop = asyncio.get_event_loop()
    print_loop.create_task(async_print())
    while True:
        try:
            event = ws.recieve(1024)
            print(event.decode())
            if event == 'JCar_on':
                print(event)
                print("movubg ig")
                await motor1.set_pwm_frequency(40000)
                await motor1.set_speed_in_percentage(100)
                await motor2.set_pwm_frequency(40000)
                await motor2.set_speed_in_percentage(100)
            elif event == 'JCar_off':
                print(event)
                await motor1.set_pwm_frequency(0)
                await motor1.set_speed_in_percentage(0)
                await motor2.set_pwm_frequency(0)
                await motor2.set_speed_in_percentage(0)
                await motor1.stop()
                await motor2.stop()
            elif event == 'JCar_forward':
                print(event)
                await motor1.move_forward()
                await motor2.move_forward()
            elif event == 'JCar_forward':
                print(event)
                await motor1.move_backward()
                await motor2.move_backward()
            time.sleep(1)
            ws.send(bytes("heollo", "utf8"))
        except Exception as e:
            print(e)
            break
        await asyncio.sleep(0.1)

# Static CSS/JSS
@app.route("/static/<path:path>")
def static(request, path):
    if ".." in path:
        # directory traversal is not allowed
        return "Not found", 404
    return send_file("static/" + path)


# shutdown
@app.get('/shutdown')
def shutdown(request):
    request.app.shutdown()
    return 'The server is shutting down...'


if __name__ == "__main__":
    try:
        app.run()
    except KeyboardInterrupt:
        pass