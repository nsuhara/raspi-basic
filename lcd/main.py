"""lcd/main.py
author          : nsuhara <na010210dv@gmail.com>
date created    : 2020/8/23
python version  : 3.7.3
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
            self.lcd.message(message='1234567890123456', line=self.lcd.LINE_1)
            self.lcd.message(message='abcdefghijklmnop', line=self.lcd.LINE_2)
            time.sleep(2)

            self.lcd.message(message='ABCDEFGHIJKLMNOP', line=self.lcd.LINE_1)
            self.lcd.message(message='ｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀ', line=self.lcd.LINE_2)
            time.sleep(2)


if __name__ == '__main__':
    raspi = Raspi()
    try:
        print('start')
        raspi.loop()
    except KeyboardInterrupt:
        raspi.destroy()
        print('stop')
