import pyaudio
import wave
from matrix_lite import led
from time import sleep
from math import pi, sin

everloop = ['black'] * led.length

color=[[219,117,0],[219,117,0],[219,117,0],[219,117,0],[0,114,207],[0,114,207],[0,114,207],[0,114,207],[255,126,185],[255,126,185],[255,126,185],[255,126,185],[176,0,170],[176,0,170],[176,0,170],[176,0,170],[51,171,0],[51,171,0],[51,171,0],[51,171,0],[144,144,144],[144,144,144],[144,144,144],[144,144,144],[255,225,0],[255,225,0],[255,225,0],[255,225,0],[242,53,136],[242,53,136],[242,53,136],[242,53,136],[255,255,255],[255,255,255],[255,255,255]]

print(led.length)

ledAdjust = 0.0
if len(everloop) == 35:
    ledAdjust = 0.51 # MATRIX Creator
else:
    ledAdjust = 1.01 # MATRIX Voice

frequency = 0.375
counter = 0.0
tick = len(everloop) - 1

# recording configs
CHUNK = 4800
FORMAT = pyaudio.paInt16
CHANNELS = 8
RATE = 96000
RECORD_SECONDS = 60*6

def Average(lst):
    return sum(lst) / len(lst)

# create & configure microphone
mic = pyaudio.PyAudio()
stream = mic.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")

# read & store microphone data per frame read
frames = []
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    data = round((7/5)*Average(data)-(140))
    if(data>=35):
        data=35
    elif(data<=0):
        data=0
    print(data)
    for i in range(data):
        colors=color[i]
        r = round(colors[0])
        g = round(colors[1])
        b = round(colors[2])
        everloop[i] = {'r':r, 'g':g, 'b':b}
    for i in range(data,35):
        r = round(0)
        g = round(0)
        b = round(0)
        everloop[i] = {'r':r, 'g':g, 'b':b}
    led.set(everloop)

print("* done recording")

# kill the mic and recording
stream.stop_stream()
stream.close()
mic.terminate()