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
        return {"temerature": temperature, "humidity": humidity}
     
    
        '''if humidity and temperature:
            return {"temerature": temperature, "humidity": humidity}
        else:
            count = 0
            while not humidity and not temperature:
                humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
                sleep(3)
                count += 1
                if count > 15:
                    raise Exception("Истёк лимит запросов, попробуйте позже.")'''
