Jarvis Bot

A simple Python-based personal assistant that uses speech recognition and text-to-speech to execute various commands, such as searching Wikipedia, opening websites, playing music, and more.

Features
	•	Speech Recognition: Recognizes voice commands using the speech_recognition library.
	•	Text-to-Speech: Uses pyttsx3 for converting text responses to speech.
	•	Wikipedia Search: Retrieves summaries of topics from Wikipedia.
	•	Web Browsing: Opens websites like YouTube, Google, and StackOverflow.
	•	Custom Commands: Execute tasks like opening Visual Studio Code and playing music on YouTube.
	•	Dynamic Greeting: Greets the user based on the current time.

Prerequisites

Before running the project, ensure you have the following installed:
	•	Python 3.x
	•	Required Python libraries:
	•	pyttsx3
	•	speech_recognition
	•	wikipedia

Install the libraries using:

pip install pyttsx3 speechrecognition wikipedia

Setup Instructions
	1.	Clone this repository:

git clone https://github.com/<your-username>/jarvis-bot.git

Replace <your-username> with your GitHub username.

	2.	Navigate to the project folder:

cd jarvis-bot


	3.	Run the bot:

python jarvis.py

How It Works
	1.	The bot greets the user dynamically based on the time of the day.
	2.	The user can issue commands like:
	•	“Open YouTube”: Opens YouTube in the default web browser.
	•	“Search Wikipedia for Python”: Retrieves a short summary about Python from Wikipedia.
	•	“Play Music”: Opens YouTube Music and starts playing music.
	•	“Open Code”: Opens Visual Studio Code.
	3.	The bot listens for commands in a loop, allowing continuous interaction.

Customizing the Bot

Add More Commands

You can add more commands by modifying the if-elif statements in the jarvis.py file. For example:

elif 'open gmail' in query:
    speak("Opening Gmail...")
    webbrowser.open("https://mail.google.com")

Change the Voice

To change the voice, update the selected_voice_id in the script:

selected_voice_id = "com.apple.voice.compact.en-GB.Daniel"  # For macOS

Limitations
	•	The bot relies on an internet connection for speech recognition and Wikipedia queries.
	•	Accuracy of voice commands depends on the clarity of the user’s speech.

Contributing

Feel free to fork the repository and submit pull requests for improvements or additional features.

License

NO Licence. Free to use and reuse

Contact

If you have any questions or suggestions, feel free to reach out:
	•	GitHub: Shreyash191911
	•	Email: shreyashkande24@gmail.com
