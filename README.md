# Final-project-JBrownnu

The main feature of this program is that it can record a 5 second audio clip and simulate it inside different locations. This simulation will then be outputted by the program so that the original recording and the simulated clip can be compared to see the difference. The other feature of the program includes giving recommendations to users based on the provided audience size and speaker equipment. There are classes created to generate each room and a method in each to create the simulation and output the audiofile. There is also another class to record and output the initial 5 second clip. 

The main file inherits methods from all 4 classes in order to allow for the simulation of all the rooms as well as record the initial audioclip. The three rooms use the audio file object from the audio class as an input in order to output the simulated audio clip. If you want to test out the program for yourself, download the zip file from github and open it in your python environment. Then after installing the listed packages run the main.py file.
- pyroomacoustics
- IPython.display
- librosa
- librosa.display 
- matplotlib.pyplot
- numpy

If one were to develop this project further, something they could do to improve the project is provide all simulated samples to the user at once, instead of only giving them the recommended sample. Another improvement to the project would be creating a room based on parameters provided by the user, and then creating a simulated sample from those parameters.
