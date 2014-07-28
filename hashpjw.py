import binascii
import sys

def hashpjw(str):
    h = 0
    g = 0
    for i in range(len(str)):
        h = (((h << 4) & 0xFFFFFFFF) + int(binascii.b2a_hex(str[i]), 16)) & 0xFFFFFFFF
        g = (h & 0xF0000000)
        if g:
            h = (h ^ (g >> 24)) & 0xFFFFFFFF
            h = (h ^ g) & 0xFFFFFFFF
    return h

if __name__ == "__main__":
    print hashpjw(sys.argv[1])
