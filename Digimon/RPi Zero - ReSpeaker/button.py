from gpiozero import Button
import os

def start():
    os.system('aplay 915.wav')

button = Button(17)
button.when_released = start

while True:
    ...