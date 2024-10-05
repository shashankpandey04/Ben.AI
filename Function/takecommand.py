import speech_recognition as recognizer
from Function.speak import speak

def takeCommand():
    """
    This function will take the command from the user
    """
    # Initialize the recognizer
    r = recognizer.Recognizer()

    with recognizer.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"User  said: {query}\n")
        return query

    except:
        return "None"