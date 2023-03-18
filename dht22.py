import dht
from machine import Pin

class DHT22:
    def load_sensor( PIN_TEMP ):
        sensor = dht.DHT22(Pin(PIN_TEMP, Pin.IN, Pin.PULL_UP))
        return sensor
