import pyroomacoustics as pra
import IPython.display as ipd
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np


'''
Generates a classroom with 1 person to simulate sound
Methods: create_classroom()
    Inputs:
        audiofile: .wav file that will be used when simulating the room
    Outputs:
        Outputs simulated .wav file 
'''

class Classroom():

    def create_classroom(audiofile):
        
        # The dimensions of the room in meters
        CLASSROOM_DIM = [8,9,4]  

        #Absorption coefficients at different centering frequencies (affects how sound travels within the room)
        classroom_tables = {
            'description': 'Rows of classroom tables and persons on chairs',
            'coeffs': [0.2, 0.3, 0.4, 0.5, 0.5, 0.6, 0.6],
            'center_freqs': [125, 250, 500, 1000, 2000, 4000, 8000],
        }
        class_materials = pra.Material(energy_absorption=classroom_tables)
    
        # Create the room
        classroom = pra.ShoeBox(CLASSROOM_DIM,fs=44100, max_order=10, materials=class_materials)

        # Turns audiofile into an array to be added to room
        audiofile_array, sampling_rate = librosa.load(audiofile, sr=44100)
        ipd.Audio(audiofile_array, rate=sampling_rate)

        # Adds person to room
        classroom.add_source([1,4.5,1.8], signal=audiofile_array)

        # Adds three microhones to the front, center, and back of the room respectively (represents audience members)
        classroom.add_microphone([3,4.5,1.8])
        classroom.add_microphone([5,4.5,1.8])
        classroom.add_microphone([7,4.5,1.8])
        
        # Creates room impulse response
        classroom.image_source_model()
        classroom.compute_rir()
        
        #plt.figure()
        #classroom.plot_rir()
        #plt.grid()
        #plt.show()

        # Starts simulation
        classroom.simulate(return_premix=True)
        
        # Generates output file
        classroom.mic_array.to_wav("Classroom_simulated_speech_recording.wav", norm=True, bitdepth=np.int16)
        ipd.Audio('Classroom_simulated_speech_recording.wav')
    
