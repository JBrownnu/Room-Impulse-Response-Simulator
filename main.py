#import pyroomacoustics as pra
from auditorium import Auditorium
from classroom import Classroom
from audio import Audio
from large_classroom import Large_Classroom


'''
Provides recommendations based on audience size and speaker equipment and outputs room simulation
Methods: Audio.record_audio()
    Inputs:
        N/A
    Outputs:
        Outputs 5 second .wav file 

'''

# Asks user for audience size
audience_size = int(input("How large is your audience for this event? Provide an integer estimate: "))

# Asks user for number of sources
number_of_sources = int(input("How many speakers do you have? Provide an integer estimate: "))

# Informs the user on how to start recording
input("Hit enter and say something into your microphone in order to record a 5 second audio file on your computer." +
"\nThis audio file will be used in the simulation.\n")

# Records audio
Audio.record_audio()

# Provides recommendation based on audience size and number of speakers
if audience_size <= 25:
    Classroom.create_classroom("speech_recording.wav")
    print("For a small group, a small classroom will work best for a speech.\n" +
    "'Classroom_simulated_speech_recording.wav is an audio file of what you would sound like in a classroom.\n")
elif 25 < audience_size <= 50:
    if number_of_sources >= 2:
        Large_Classroom.create_large_classroom("speech_recording.wav")
        print("With two or more speakers, a large classroom will work best for a speech.\n" +
        "'Large_Classroom_simulated_speech_recording2.wav is an audio file of what you would sound like in a classroom.\n")
    else:
        Classroom.create_classroom("speech_recording.wav")
        print("Without more speakers, a small classroom will work best for a speech.\n" +
        "'Classroom_simulated_speech_recording.wav is an audio file of what you would sound like in a classroom.\n")
else:
    if number_of_sources >= 8:
        Auditorium.create_auditorium("speech_recording.wav")
        print("With so many speakers, an auditorium will work best for a speech\n" +
        "'Auditorium_simulated_speech_recording.wav is an audio file of what you would sound like in a classroom.\n4")
    else:
        print("Too many people and not enough speakers! Find more equipment or lower the expected audience size")



    

