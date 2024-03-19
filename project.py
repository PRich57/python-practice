import csv
import nltk
import spacy
import string

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('stopwords')

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

def main():
    transcript = input("Enter your transcript: ")
    processed_transcript = process_transcript(transcript)
    action_words = extract_actions(processed_transcript)
    export_to_csv(action_words)


# Process the transcript to remove filler words and return cleaned text
def process_transcript(transcript):
    # Lowercase the transcript for consistent processing
    transcript = transcript.lower()

    # Define list of filler words to remove
    filler_words = {'uh', 'um', 'ah', 'like', 'so', 'you know', 'actually', 'basically', 'seriously', 'literally'}

    # Load English stopwords, then remove certain words to preserve sentence structure
    stopwords_list = set(stopwords.words('english')) - {'and', 'but', 'or', 'as', 'if', 'when', 'than', 'because', 'while', 'where', 'after', 'so', 'though', 'since', 'until', 'whether', 'before', 'although', 'nor', 'like', 'once', 'unless', 'now', 'except'}

    # Combine filler words with English stopwords from NLTK
    stopwords_combined = stopwords_list.union(filler_words)

    # Tokenize transcript into words
    words = word_tokenize(transcript)

    # Filter out filler words and stopwords from the transcript
    filtered_words = [word for word in words if word not in stopwords_combined and word not in string.punctuation]

    # Join the filtered words back into a string
    processed_transcript = ' '.join(filtered_words).capitalize()

    # print(processed_transcript)

    return processed_transcript


# Extract action words or phrases from the processed text
def extract_actions(text):
    # Process the text with spaCy
    doc = nlp(text)

    # Extract words that are tagged as verbs
    action_words = [print(token.pos_, token.text) for token in doc]

    return action_words


# Exports the action words to a CSV file
def export_to_csv(action_words):
    with open('action_words.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Action Words"])
        for word in action_words:
            writer.writerow([word])


if __name__ == "__main__":
    main()