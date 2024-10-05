import pyttsx3

# Initialize the pyttsx3 engine
engine = pyttsx3.init('sapi5')

# Get the voices and set the voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    """
    This function will speak the audio.
    :param audio: str -> The audio to be spoken
    """
    engine.say(audio)
    engine.runAndWait()