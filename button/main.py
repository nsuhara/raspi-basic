"""button/main.py
author          : nsuhara <na010210dv@gmail.com>
date created    : 2020/8/23
python version  : 3.7.3
"""

from signal import pause

from gpiozero import Button


class Raspi():
    """Raspi
    """
    GPIO_BCM_BUTTON1 = 15
    GPIO_BCM_BUTTON2 = 25

    def __init__(self):
        self.button1 = Button(self.GPIO_BCM_BUTTON1)
        self.button1.when_pressed = self.button1_pressed
        self.button1.when_released = self.button1_released

        self.button2 = Button(self.GPIO_BCM_BUTTON2)
        self.button2.when_pressed = self.button2_pressed
        self.button2.when_released = self.button2_released

    def button1_pressed(self):
        """button1_pressed
        """
        print('>>> button1_pressed')

    def button1_released(self):
        """button1_released
        """
        print('>>> button1_released')

    def button2_pressed(self):
        """button2_pressed
        """
        print('>>> button2_pressed')

    def button2_released(self):
        """button2_released
        """
        print('>>> button2_released')

    def pause(self):
        """pause
        """
        pause()


if __name__ == '__main__':
    raspi = Raspi()
    try:
        print('start')
        raspi.pause()
    except KeyboardInterrupt:
        print('stop')
