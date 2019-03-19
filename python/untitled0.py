# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 17:44:56 2018

@author: Window
"""
import numpy as np
import pyaudio 
import time
def start_stream(callback):
    p = pyaudio.PyAudio()
    frames_per_buffer = int(44100 / 60)
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=44100,
                    input=True,
                    frames_per_buffer=frames_per_buffer)
    overflows = 0
    prev_ovf_time = time.time()
    while True:
        try:
            y = np.frombuffer(stream.read(frames_per_buffer), dtype=np.int16)
            y = y.astype(np.float32)
            callback(y)
        except IOError:
            overflows += 1
            if time.time() > prev_ovf_time + 1:
                prev_ovf_time = time.time()
                print('Audio buffer has overflowed {} times'.format(overflows))
    stream.stop_stream()
    stream.close()
    p.terminate()
    
def microphone_update(audio_samples):
    global y_roll, prev_rms, prev_exp, prev_fps_update
    # Normalize samples between 0 and 1
    y = audio_samples / 2.0**15
    # Construct a rolling window of audio samples
    y_roll[:-1] = y_roll[1:]
    y_roll[-1, :] = np.copy(y)
    y_data = np.concatenate(y_roll, axis=0).astype(np.float32)
samples_per_frame = int(44100 / 60)
y_roll = np.random.rand(2, samples_per_frame) / 1e16
print(y_roll)
print(type(y_roll))
start_stream(microphone_update)
