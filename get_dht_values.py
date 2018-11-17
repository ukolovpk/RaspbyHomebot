import sys
from time import sleep
import Adafruit_DHT


class DHTValues(object):
    
    def __init__(self, pin=4, sensor=11):
        self.pin = pin
        self.sensor = sensor
    
    def get_temperature_and_humidity(self):
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        count = 0
        try:
            assert humidity and temperature
        except:
            while count < 15:
                humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
                if humidity and temperature:
                    return {"humidity": humidity, "temperature": temperature}
                else:
                    count += 1
                    sleep(3)
        return {"temperature": temperature, "humidity": humidity}
