
from Function.takecommand import takeCommand
from Function.wish import wish
from Function.wikipedia import fetch_wikipedia_content, summarize_text
from Function.speak import speak

SLEEP = False

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
        elif "search" in query:
                speak("Hmm, let me check that for you.")
                speak(f"Searching Wikipedia for {query}")
                query = query.replace("wikipedia", "")

                # Fetch Wikipedia content
                wiki_content = fetch_wikipedia_content(query)
                speak("Summarizing the content from Wikipedia.")
                # Summarize the Wikipedia content
                summarized_content = summarize_text(wiki_content, max_length=50)
                speak("Here is a summary of the article:")
                speak(summarized_content)

        else:
            speak("Sorry, I did not get that. Please try again.")

if __name__ == "__main__":
    main()
