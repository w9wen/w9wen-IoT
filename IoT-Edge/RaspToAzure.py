import time
import Adafruit_DHT
import RPi.GPIO as gpio

sensor = Adafruit_DHT.DHT22
sensor_pin = 27

humidity, temperature = Adafruit_DHT.read_retry(sensor, sensor_pin)

if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
else:
    print('Failed to get reading')

led_pin = 22
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(led_pin, gpio.OUT)

for target_list in range(5):
    gpio.output(led_pin, gpio.HIGH)
    time.sleep(0.5)
    gpio.output(led_pin, gpio.LOW)
    time.sleep(0.5)