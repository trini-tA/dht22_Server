import utime as time
from server import Server
from dht22 import DHT22
from ifconfig import IFCONFIG
import socket
import json

VERSION = "0.1"
NAME = "TSRV"
DISPLAY_NAME = NAME + " " + VERSION
PIN_TEMP = 2                # on board -> D4

time.sleep(2)

# network
ip_address = IFCONFIG.get_address()
short_ip_address = ip_address.split( '.' )

# Server
time.sleep(2)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip_address, 80))
s.listen(1)

print( 'ip_address:: ', ip_address )

# measure
d = DHT22.load_sensor( PIN_TEMP )
count = 0

output_html = True

while True:
    cl, addr = s.accept()
    print('client connected from', addr)
    cl_file = cl.makefile('rwb', 0)
    request = cl.recv(2048)
    parseRequest = request.decode('utf-8').split(' ')

    if parseRequest[0] == 'GET':
        params = parseRequest[1]
        if params == '/html':
            output_html = True

        if params == '/json':
            output_html = False

    # Response
    d.measure()
    time.sleep(2) # wait !
    temp = d.temperature()
    hum = d.humidity()
    count = count + 1

    sensors = [
        {
            'datetime': None,
            'deviceName': "esp8266-dht-22-sensors",
            'temperature': float(temp),
            'pressure': float(0.0),
            'humidity': float(hum),
            'isValid': True
        }
    ]

    if output_html:
        html = ''
        for data in sensors:
            html = html + '<div><label>{}</label><span class="class-{}">{}</span></div>\n'.format(data.get('name'),
                                                                                                  data.get('name'),
                                                                                                  data.get('value'))
        response = Server.template(DISPLAY_NAME) % html
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n'.encode())
    else:
        response = json.dumps( sensors )
        cl.send('HTTP/1.0 200 OK\r\nContent-type: application/json\r\n\r\n'.encode())

    cl.send(response.encode())
    cl.close()





