import numpy as np
import pyaudio
import struct
import wave

import os

BLOCKSIZE = 128

# Get recording parameters
RATE     = 22050
WIDTH    = 2
CHANNELS = 1
LEN      = 1 * RATE

def is_silent(data, THRESHOLD):
    "Returns 'True' if below the threshold"
    return max(data) < THRESHOLD

def record(path):
    
    # Output wave file
    output_wf = wave.open('orig_data/' + path, 'w')
    # output_wf = wave.open('222/-1_richard_22.wav', 'w')
    output_wf.setframerate(RATE)
    output_wf.setsampwidth(WIDTH)
    output_wf.setnchannels(CHANNELS)

    p = pyaudio.PyAudio()
    stream = p.open(format = p.get_format_from_width(WIDTH),
                    channels = CHANNELS,
                    rate = RATE,
                    input = True,
                    output = True)
    
    # Wait until voice detected
    while True:    
        input_string = stream.read(BLOCKSIZE, exception_on_overflow = False)
        input_value = struct.unpack('h' * BLOCKSIZE, input_string)
        silent = is_silent(input_value, 2000)
        if not silent:
            break

        # Start recording
    print("Recording Start")

    nBLOCK = int(LEN / BLOCKSIZE)
    numSilence = 0
    for n in range(0, nBLOCK + 1):
        
        if is_silent(input_value, 100):
            numSilence += 1
#            output_value = np.zeros(BLOCKSIZE) 
 
        output_value = np.array(input_value)
        
        if numSilence > 14:
            break
        
        output_value = output_value.astype(int)
        output_value = np.clip(output_value, -2**15, 2**15 - 1)

        ouput_string = struct.pack('h' * BLOCKSIZE, *output_value)
        output_wf.writeframes(ouput_string)
        
        input_string = stream.read(BLOCKSIZE, exception_on_overflow = False)
        input_value = struct.unpack('h' * BLOCKSIZE, input_string)

    print('Recording End')

    stream.stop_stream()
    stream.close()
    p.terminate()
    output_wf.close()

import time
ts = time.time()
import datetime
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')

name = "aidan"

print("Record your \"left\" samples")

import time

# for x in range(200):
#     ts = time.time()
#     st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')
#     print("Ready", x,"/25")
#     left_filename = "left/left_{}{}.wav".format(name, st)
#     record(left_filename)
#     os.system('cls')  # For Windows
#     # time.sleep(1)

print("Record your \"right\" samples")

for x in range(175):
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')
    print("Ready",x,"/25")
    right_filename = "right/right{}{}.wav".format(name, st)
    record(right_filename)
    os.system('cls')  # For Windows
    # time.sleep(1)