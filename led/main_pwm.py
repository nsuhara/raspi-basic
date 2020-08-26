"""led/main_pwm.py
author          : nsuhara <na010210dv@gmail.com>
date created    : 2020/8/23
python version  : 3.7.3
"""

import time

import RPi.GPIO as GPIO

GPIO_BOARD_LED = 11


class Raspi():
    """Raspi
    """

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(GPIO_BOARD_LED, GPIO.OUT)
        GPIO.output(GPIO_BOARD_LED, GPIO.LOW)
        self.pwm_led = GPIO.PWM(GPIO_BOARD_LED, 50)
        print('using pin {}'.format(GPIO_BOARD_LED))
        print('pulse width modulation {} Hz'.format(50))

    def destroy(self):
        """destroy
        """
        self.pwm_led.stop()
        GPIO.cleanup()

    def loop(self):
        """loop
        """
        self.pwm_led.start(0)
        while True:
            self.pwm_led.ChangeDutyCycle(25)
            print('>>> 25%')
            time.sleep(1)
            self.pwm_led.ChangeDutyCycle(50)
            print('>>> 50%')
            time.sleep(1)
            self.pwm_led.ChangeDutyCycle(75)
            print('>>> 75%')
            time.sleep(1)
            self.pwm_led.ChangeDutyCycle(100)
            print('>>> 100%')
            time.sleep(1)


if __name__ == '__main__':
    raspi = Raspi()
    try:
        print('start')
        raspi.loop()
    except KeyboardInterrupt:
        raspi.destroy()
        print('stop')
