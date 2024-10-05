
import wikipedia
import torch
from transformers import pipeline


# Function to summarize text using a pre-trained model (BART or T5)
def summarize_text(text, max_length=150):
    """
    This function will summarize the text using a pre-trained model.
    :param text: str -> The text to be summarized
    :param max_length: int -> The maximum length of the summary
    :return: str -> The summarized text
    """
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length=max_length, min_length=30, do_sample=False)
    return summary[0]['summary_text']

# Function to fetch content from Wikipedia
def fetch_wikipedia_content(query):
    """
    This function will fetch the content from Wikipedia.
    :param query: str -> The query to search on Wikipedia
    :return: str -> The content from Wikipedia
    """
    try:
        summary = wikipedia.summary(query, sentences=4)
        summary = summary[:summary.rfind('.')+1]
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        summary = wikipedia.summary(e.options[0], sentences=4)
        summary = summary[:summary.rfind('.')+1]
    except wikipedia.exceptions.PageError:
        return "Sorry, I could not find any relevant information on Wikipedia."