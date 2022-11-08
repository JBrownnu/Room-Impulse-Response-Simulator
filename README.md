# Final-project-JBrownnu

1. Who is on your team? If you are working with a partner, how will the labor be divided? 
- I will be on a team by myself
2. An overview of the project similar in scope and length to the example projects listed below.
- My project would be a room acoustic simulation program. The program will take in a sound clip as an input, and simulate the sound being played in a different environment, such as a lecture hall or auditorium. The program will be able to use this information to give recommendations on a desired environment for an event or speech given the amount of sound equipment available (number of microphones being used at once and the number of speakers available)

3. A short description of the structure of your project. How many classes will you write? What the methods be for each class? (You can change this if it turns out a better structure would work better once you start writing code and you decide to refactor. Just try to come up with a reasonable one for the proposal.)
- A class representing the room being simulated as well
- 	A simulation method is used to create the room
- 	A method used to add the sources and microphones to the room
- A class representing the sources or speakers within the room that will play the given sound clip
- A class representing the microphones within the room
- A class representing the directivity of the speakers and microphones from each other
- 	A directivity method will be created 
- Parent class to run the simulation
- 	Method to simulate the sound in the room
- 	Method to print recommendations on room to the user based on room impulse response (plot of how the sound is simulated within the room)

4. What libraries and tools will you need to learn to use?
- Numpy library for mathematical computations 
- matplotlib.pyplot plotting room impulse response
- pyroomacoustics for room simulation
- scipy.io for playing sound clip

5. Identify the highest-priority features, the medium-priority features, and the lowest-priority features for your project.
- Highest Priority:
- 	Simulating how the sound clip will sound in different environments
- Medium Priority:
- 	Giving recommendations to user based on sound equipment
- Lowest Priority:
- 	Give recommendations to user based on audience size
