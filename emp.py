import RPi.GPIO2 as GPIO
import time

S0 = 17
S1 = 27
S2 = 22
S3 = 23
OUT = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(S0, GPIO.OUT)
GPIO.setup(S1, GPIO.OUT)
GPIO.setup(S2, GPIO.OUT)
GPIO.setup(S3, GPIO.OUT)
GPIO.setup(OUT, GPIO.IN)

def get_color():
    # Set sensor to read red color
    GPIO.output(S2, GPIO.LOW)
    GPIO.output(S3, GPIO.LOW)
    time.sleep(0.3)
    red = GPIO.input(OUT)

    # Set sensor to read green color
    GPIO.output(S2, GPIO.HIGH)
    GPIO.output(S3, GPIO.HIGH)
    time.sleep(0.3)
    green = GPIO.input(OUT)

    # Set sensor to read blue color
    GPIO.output(S2, GPIO.LOW)
    GPIO.output(S3, GPIO.HIGH)
    time.sleep(0.3)
    blue = GPIO.input(OUT)

    if red == 1 and green == 0 and blue == 0:
        return "Red"
    elif red == 1 and green == 1 and blue == 0:
        return "Yellow"
    elif red == 0 and green == 1 and blue == 0:
        return "Green"
    elif red == 0 and green == 1 and blue == 1:
        return "Cyan"
    elif red == 0 and green == 0 and blue == 1:
        return "Blue"
    elif red == 1 and green == 0 and blue == 1:
        return "Magenta"