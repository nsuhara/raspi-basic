"""motor/main.py
"""

from time import sleep

import RPi.GPIO as GPIO

GPIO_BCM_L293D_EN1 = 17
GPIO_BCM_L293D_IN1 = 27
GPIO_BCM_L293D_IN2 = 22


def setup():
    # GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_BCM_L293D_EN1, GPIO.OUT)
    GPIO.setup(GPIO_BCM_L293D_IN1, GPIO.OUT)
    GPIO.setup(GPIO_BCM_L293D_IN2, GPIO.OUT)


def right():
    GPIO.output(GPIO_BCM_L293D_EN1, GPIO.HIGH)
    GPIO.output(GPIO_BCM_L293D_IN1, GPIO.LOW)
    GPIO.output(GPIO_BCM_L293D_IN2, GPIO.HIGH)


def left():
    GPIO.output(GPIO_BCM_L293D_EN1, GPIO.HIGH)
    GPIO.output(GPIO_BCM_L293D_IN1, GPIO.HIGH)
    GPIO.output(GPIO_BCM_L293D_IN2, GPIO.LOW)


def stop():
    GPIO.output(GPIO_BCM_L293D_EN1, GPIO.LOW)


def destroy():
    GPIO.cleanup()


if __name__ == '__main__':
    setup()
    try:
        right()
        sleep(2)
        left()
        sleep(2)
        stop()
    except KeyboardInterrupt:
        destroy()
