#!/home/pi/projects/magicbandreader/virtual_env/bin/python3

from time import sleep

import board
import neopixel

COLOR_GREEN = (255,0,0) 

COLOR_WHITE = (255, 255, 255)

COLOR_RED = (0, 255, 0)

# GPIO Pin (Recommend GPIO18)
pixel_pin = board.D18

RING_COUNT = 53
FACE_COUNT = 41

INTERVAL = 1.0

def main():
    print("start")
    # pixels = neopixel.NeoPixel(pixel_pin, TOTAL_PIXELS, brightness=1.0, auto_write=False, pixel_order=neopixel.RGB)
    total_leds = FACE_COUNT + RING_COUNT
    pixels = neopixel.NeoPixel(pixel_pin, total_leds, auto_write=False, pixel_order=neopixel.RGB)

    while True:
        for mode in ["FACE", "RING", "ALL"]:
            print(mode)
            for color, name in [
                [COLOR_GREEN, "green"],
                [COLOR_RED, "red"],
                [COLOR_WHITE, "White"]
            ]:
                face_color = color if mode in ["FACE", "ALL"] else 0
                ring_color = color if mode in ["RING", "ALL"] else 0
                for pixel in range(0,RING_COUNT):
                    pixels[pixel] = ring_color
                for pixel in range(0, FACE_COUNT):
                    pixels[pixel + RING_COUNT] = face_color
                print("commit")
                pixels.show()
                sleep(INTERVAL)

                print("off")
                print("commit one at a time")
                for i in range(total_leds):
                    pixels[i] = 0
                    pixels.show()
                sleep(INTERVAL)

    print("DONE")

if __name__ == "__main__":
    main()
