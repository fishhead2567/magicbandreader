import time

import RPi.GPIO as GPIO


PIN = 12

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PIN, GPIO.OUT) # LED 1
    print("Pin is hot")
    GPIO.output(PIN, GPIO.HIGH)
    time.sleep(30)


if __name__ == "__main__":
    main()
