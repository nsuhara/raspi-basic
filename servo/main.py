"""servo/main.py
author          : nsuhara <na010210dv@gmail.com>
date created    : 2020/8/23
python version  : 3.7.3
"""

import time

import RPi.GPIO as GPIO

GPIO_BOARD_SERVO = 18


class Raspi():
    """Raspi
    """

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(GPIO_BOARD_SERVO, GPIO.OUT)
        GPIO.output(GPIO_BOARD_SERVO, GPIO.LOW)
        self.pwm_servo = GPIO.PWM(GPIO_BOARD_SERVO, 50)
        print('using pin {}'.format(GPIO_BOARD_SERVO))
        print('pulse width modulation {} Hz'.format(50))

    def destroy(self):
        """destroy
        """
        self.pwm_servo.stop()
        GPIO.cleanup()

    def angle(self, angle):
        """angle
        """
        duty = 2.5 + (12.0 - 2.5) * (angle + 90) / 180
        self.pwm_servo.ChangeDutyCycle(duty)
        time.sleep(0.3)

    def loop(self):
        """loop
        """
        self.pwm_servo.start(0)
        while True:
            self.angle(0)
            print('>>> 0°')
            self.angle(-60)
            print('>>> -60°')
            self.angle(0)
            print('>>> 0°')
            self.angle(60)
            print('>>> +60°')


if __name__ == '__main__':
    raspi = Raspi()
    try:
        print('start')
        raspi.loop()
    except KeyboardInterrupt:
        raspi.destroy()
        print('stop')
