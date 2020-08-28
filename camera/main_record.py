"""camera/main_record.py
author          : nsuhara <na010210dv@gmail.com>
date created    : 2020/8/23
python version  : 3.7.3
"""

from signal import pause


from picamera import PiCamera


class Raspi():
    """Raspi
    """

    def __init__(self):
        self.camera = PiCamera()

    def start(self):
        """start
        """
        self.camera.start_preview()
        self.camera.start_recording('camera.h264')
        pause()

    def stop(self):
        """stop
        """
        self.camera.stop_recording()
        self.camera.stop_preview()


if __name__ == '__main__':
    raspi = Raspi()
    try:
        print('start')
        raspi.start()
    except KeyboardInterrupt:
        raspi.stop()
        print('stop')
