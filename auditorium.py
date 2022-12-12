import pyroomacoustics as pra
import IPython.display as ipd
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

'''
Generates an auditorium with 8 loudspeakers and 1 person to simulate sound
Methods: create_auditorium()
    Inputs:
        audiofile: .wav file that will be used when simulating the room
    Outputs:
        Outputs simulated .wav file 
'''

class Auditorium():
    
    def create_auditorium(audiofile):
        
        # The dimensions of the room in meters
        AUDITORIUM_DIM = [40,30,25]  

        #Absorption coefficients at different centering frequencies (affects how sound travels within the room)
        theatre_audience = {
            'description': 'Theatre Audience setup',
            'coeffs': [0.3, 0.5, 0.6, 0.6, 0.7, 0.7, 0.7],
            'center_freqs': [125, 250, 500, 1000, 2000, 4000, 8000],
        }
        auditorium_materials = pra.Material(energy_absorption=theatre_audience)
    
        # Create the room
        auditorium = pra.ShoeBox(AUDITORIUM_DIM,materials=auditorium_materials, fs=44100, max_order=10)
        
        # Turns audiofile into an array to be added to room
        audiofile_array, sampling_rate = librosa.load(audiofile, sr=44100)
        ipd.Audio(audiofile_array, rate=sampling_rate)
        
        # Adds person to room
        auditorium.add_source([4.5,15,3], signal=audiofile_array)

        #Adds 8 loudspeakers to room
        auditorium.add_source([5,5,1.8], signal=audiofile_array)
        auditorium.add_source([5,6,1.8], signal=audiofile_array)
        auditorium.add_source([5,15,1.8], signal=audiofile_array)
        auditorium.add_source([5,16,1.8], signal=audiofile_array)
        auditorium.add_source([5,25,1.8], signal=audiofile_array)
        auditorium.add_source([5,26,1.8], signal=audiofile_array)
        auditorium.add_source([5,10,22], signal=audiofile_array)
        auditorium.add_source([5,20,22], signal=audiofile_array)

        # Adds three microhones to the front, center, and back of the room respectively (represents audience members)
        auditorium.add_microphone([12,15,1.8])
        auditorium.add_microphone([24,15,1.8])
        auditorium.add_microphone([36,15,1.8])

        # Creates room impulse response
        auditorium.image_source_model()
        auditorium.compute_rir()
        
        #plt.figure()
        #auditorium.plot_rir()
        #plt.grid()
        #plt.show()

        # Starts simulation
        auditorium.simulate()

        # Generates output file
        auditorium.mic_array.to_wav("Auditorium_simulated_speech_recording3.wav", norm=True, bitdepth=np.int16)
        ipd.Audio('Auditorium_simulated_speech_recording3.wav')
    


    