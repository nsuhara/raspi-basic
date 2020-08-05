"""blink_led/main.py
"""

import time

import RPi.GPIO as GPIO

LED_PIN = 11


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN, GPIO.LOW)
    print('using pin {}'.format(LED_PIN))


def destroy():
    GPIO.cleanup()


def loop():
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)
        print('on')
        time.sleep(1)
        GPIO.output(LED_PIN, GPIO.LOW)
        print('off')
        time.sleep(1)


if __name__ == '__main__':
    setup()
    try:
        print('start')
        loop()
    except KeyboardInterrupt:
        destroy()
        print('stop')
