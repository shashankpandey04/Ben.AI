
from Function.takecommand import takeCommand
from Function.wish import wish
#from Function.wikipedia import fetch_wikipedia_content, summarize_text
from Function.speak import speak

import os
import dotenv

import google.generativeai as genai

dotenv.load_dotenv()

SLEEP = False

GEMINI_API = os.getenv("API_KEY")

genai.configure(api_key=GEMINI_API)
model = genai.GenerativeModel(model_name='gemini-1.5-flash')

def main():
    """
    The main function to run the application
    """

    speak(wish())

    speak("I am Ben. How can I help you?")
    
    while True:
        query = takeCommand().lower()
        if query == "none":
            continue

        elif "what is" and "weather" in query:
            speak("I am checking the weather for you.")
            response = model.generate_content(query)
            speak(response.text)
        
        else:
            response = model.generate_content(query)
            speak(response.text)

if __name__ == "__main__":
    main()
