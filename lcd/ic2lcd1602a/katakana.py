"""ic2lcd1602a/katakana.py
"""

SP_CODE = 0xfec0


def convert(message):
    """convert
    """
    converted = []
    for char in message:
        if ord(char) > SP_CODE:
            converted.append(chr(ord(char)-SP_CODE))
        else:
            converted.append(char)
    return ''.join(converted)
