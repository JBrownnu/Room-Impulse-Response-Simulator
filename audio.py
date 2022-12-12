#import pyroomacoustics as pra
#import IPython.display as ipd
#import librosa.display
#import matplotlib.pyplot as plt

import sounddevice
import soundfile


'''
Records a 5 second audio clip and saves it as a .wav file
Methods: record_audio()
    Inputs:
        N/A
    Outputs:
        Outputs 5 second .wav file 
'''

class Audio():

    def record_audio():
        
        # Initializes sample rate, duration, and filename of 5 second recording
        SAMPLERATE = 44100  # Hertz
        DURATION = 5  # seconds
        FILENAME = 'speech_recording.wav'
        
        # Records 5 second clip
        recording = sounddevice.rec(int(SAMPLERATE * DURATION), samplerate=SAMPLERATE, channels=1, blocking=True)
                
        # Saves the 5 second clip as a .wav file
        soundfile.write(FILENAME, recording, SAMPLERATE)




 