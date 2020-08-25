"""ic2lcd1602a/pcf8574t.py
"""
import time

from smbus import SMBus

from ic2lcd1602a.katakana import convert


class LCD():
    """LCD
    """
    SMBUS_REV1 = 0
    SMBUS_REV2 = 1

    I2C_ADDR = 0x27

    ENABLE_BIT = 0b00000100

    LINE_1 = 0x80
    LINE_2 = 0xC0
    LINE_SIZE = 16

    MODE_COMMAND = 0
    MODE_CHAR = 1
    MODE_OPTION_BACKLIGHT = 0x08

    CMD_INITIALISE = 0x33
    CMD_SET_4_BIT_MODE = 0x32
    CMD_CURSOR_MOVE_DIRECTION = 0x06
    CMD_TURN_CURSOR_OFF = 0x0C
    CMD_2_LINE_DISPLAY = 0x28
    CMD_CLEAR_DISPLAY = 0x01
    CMD_WAIT = 0.0005

    def __init__(self):
        self.smbus = SMBus(self.SMBUS_REV2)

        self._send(self.MODE_COMMAND, self.CMD_INITIALISE)
        self._send(self.MODE_COMMAND, self.CMD_SET_4_BIT_MODE)
        self._send(self.MODE_COMMAND, self.CMD_CURSOR_MOVE_DIRECTION)
        self._send(self.MODE_COMMAND, self.CMD_TURN_CURSOR_OFF)
        self._send(self.MODE_COMMAND, self.CMD_2_LINE_DISPLAY)
        self._send(self.MODE_COMMAND, self.CMD_CLEAR_DISPLAY)

    def destroy(self):
        """destroy
        """
        self._send(self.MODE_COMMAND, self.CMD_CLEAR_DISPLAY)

    def message(self, message, line):
        """message
        """
        message = convert(message)
        message = message[0:self.LINE_SIZE]
        message = message.ljust(self.LINE_SIZE, ' ')

        self._send(self.MODE_COMMAND | self.MODE_OPTION_BACKLIGHT, line)

        for char in message:
            self._send(self.MODE_CHAR | self.MODE_OPTION_BACKLIGHT, ord(char))

    def clear(self):
        """close
        """
        self._send(self.MODE_COMMAND | self.MODE_OPTION_BACKLIGHT,
                   self.CMD_CLEAR_DISPLAY)

    def off(self):
        """off
        """
        self._send(self.MODE_COMMAND, self.CMD_CLEAR_DISPLAY)

    def _send(self, mode, bits):
        """_send
        """
        higher_bits = mode | (bits & 0xF0)
        self._write(higher_bits)

        lower_bit = mode | ((bits << 4) & 0xF0)
        self._write(lower_bit)

    def _write(self, bits):
        """_write
        """
        self.smbus.write_byte(self.I2C_ADDR, bits)
        time.sleep(self.CMD_WAIT)

        self.smbus.write_byte(self.I2C_ADDR, (bits | self.ENABLE_BIT))
        time.sleep(self.CMD_WAIT)

        self.smbus.write_byte(self.I2C_ADDR, (bits & ~self.ENABLE_BIT))
        time.sleep(self.CMD_WAIT)

    def loop(self):
        """loop
        """

        while True:
            self.message('1234567890123456', self.LINE_1)
            self.message('abcdefghijklmnop', self.LINE_2)
            time.sleep(3)

            self.message('ABCDEFGHIJKLMNOP', self.LINE_1)
            self.message('ｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀ', self.LINE_2)
            time.sleep(3)


if __name__ == '__main__':
    lcd = LCD()
    try:
        print('start')
        lcd.loop()
    except KeyboardInterrupt:
        lcd.destroy()
        print('stop')
