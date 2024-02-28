# Spotify Search App
This document provides details on how to implement a simple program to search for albums on Spotify using Python.

# Prerequisites
	•	A Spotify account
	•	Python installed on your computer
	•	Spotipy Python library installed. You can install it using the following command:

# Install Python
- Ensure Python is installed on your computer. 
1. To set up python locally, first check to see if it's already installed by opening your CLI (commmand line interface) and inputting python --version or python3 --version.
2. If you do not have python installed, refer to this website: https://www.python.org/ and following the installation instructions for your operating system.
3. Once this is complete, ensure that its installation directory is added to your PATH environment varibale. This will enable your shell to find the "python" command.
4. To ensure step 3 is complete, in your terminal, type in "echo $PATH" to verify that the directory  (where python is installed) is included in the output.
5. Once this is complete you can install:

pip install spotipy

# Next Steps
	1	Go to Spotify Developer Dashboard and create a new client ID.
	2	Once you have created the client ID, note down the client ID and client secret.
	3	Install spotipy using the command mentioned in prerequisites.
	4	Use you client ID and client secret to place into the file: spotifysecrets.py.
