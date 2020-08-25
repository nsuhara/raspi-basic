"""lcd/main.py
"""

import time

from i2clcd1602a.pcf8574t import LCD


class Raspi():
    """Raspi
    """

    def __init__(self):
        self.lcd = LCD()

    def destroy(self):
        """destroy
        """
        self.lcd.off()

    def loop(self):
        """loop
        """
        while True:
            self.lcd.message('1234567890123456', self.lcd.LINE_1)
            self.lcd.message('abcdefghijklmnop', self.lcd.LINE_2)
            time.sleep(2)

            self.lcd.message('ABCDEFGHIJKLMNOP', self.lcd.LINE_1)
            self.lcd.message('ｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀ', self.lcd.LINE_2)
            time.sleep(2)


if __name__ == '__main__':
    raspi = Raspi()
    try:
        print('start')
        raspi.loop()
    except KeyboardInterrupt:
        raspi.destroy()
        print('stop')
