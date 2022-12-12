import pyroomacoustics as pra
import IPython.display as ipd
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np


'''
Generates a large classroom with 1 person and 2 speakers to simulate sound
Methods: create_large_classroom()
    Inputs:
        audiofile: .wav file that will be used when simulating the room
    Outputs:
        Outputs simulated .wav file 
'''

class Large_Classroom():

    def create_large_classroom(audiofile):
        
       # The dimensions of the room in meters
       LARGE_CLASSROOM_DIM = [16,18,8] 

       #Absorption coefficients at different centering frequencies (affects how sound travels within the room)
       classroom_tables = {
            'description': 'Rows of classroom tables and persons on chairs',
            'coeffs': [0.2, 0.3, 0.4, 0.5, 0.5, 0.6, 0.6],
            'center_freqs': [125, 250, 500, 1000, 2000, 4000, 8000],
        }
       large_class_materials = pra.Material(energy_absorption=classroom_tables)
    
       # Create the room
       large_classroom = pra.ShoeBox(LARGE_CLASSROOM_DIM,materials=large_class_materials, fs=44100, max_order=10)

       # Turns audiofile into an array to be added to room
       audiofile_array, sampling_rate = librosa.load(audiofile, sr=44100)
       ipd.Audio(audiofile_array, rate=sampling_rate)

       # Adds person to room
       large_classroom.add_source([1,3,6], signal=audiofile_array)

       # Adds 2 loudspeakers to room
       large_classroom.add_source([1,9,1.8], signal=audiofile_array)
       large_classroom.add_source([1,15,6], signal=audiofile_array)

       # Adds three microhones to the front, center, and back of the room respectively (represents audience members)
       large_classroom.add_microphone([3,9,1.8])
       large_classroom.add_microphone([9,9,1.8])
       large_classroom.add_microphone([15,9,1.8])

       # Creates room impulse response 
       large_classroom.image_source_model()
       large_classroom.compute_rir()
       
       #plt.figure()
       #large_classroom.plot_rir()
        #plt.grid()
       #plt.show()

       # Starts simulation
       large_classroom.simulate()
       
       # Generates output file
       large_classroom.mic_array.to_wav("Large_Classroom_simulated_speech_recording.wav", norm=True, bitdepth=np.int16)
       ipd.Audio('Large_Classroom_simulated_speech_recording.wav')