"""led/main.py
author          : nsuhara <na010210dv@gmail.com>
date created    : 2020/8/23
python version  : 3.7.3
"""

import time

import RPi.GPIO as GPIO

GPIO_BOARD_LED = 11


def setup():
    """setup
    """
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(GPIO_BOARD_LED, GPIO.OUT)
    GPIO.output(GPIO_BOARD_LED, GPIO.LOW)
    print('using pin {}'.format(GPIO_BOARD_LED))


def destroy():
    """destroy
    """
    GPIO.cleanup()


def loop():
    """loop
    """
    while True:
        GPIO.output(GPIO_BOARD_LED, GPIO.HIGH)
        print('>>> on')
        time.sleep(1)
        GPIO.output(GPIO_BOARD_LED, GPIO.LOW)
        print('>>> off')
        time.sleep(1)


if __name__ == '__main__':
    setup()
    try:
        print('start')
        loop()
    except KeyboardInterrupt:
        destroy()
        print('stop')
