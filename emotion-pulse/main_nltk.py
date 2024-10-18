import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import nltk

# Ensure necessary NLTK resources are downloaded
nltk.download('stopwords')
nltk.download('vader_lexicon')
nltk.download('punkt_tab')
nltk.download('wordnet')

# Reading the input text file
with open('read.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Text preprocessing: converting to lowercase and removing punctuation
lower_case = text.lower()
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

# Tokenizing the text
tokenized_words = word_tokenize(cleaned_text)

# Removing stopwords and lemmatizing words in one step
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

final_words = [lemmatizer.lemmatize(word) for word in tokenized_words if word not in stop_words]

# Emotion analysis based on the 'emotions.txt' file
emotion_list = []
try:
    with open('emotions.txt', 'r') as file:
        for line in file:
            clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
            if ":" in clear_line:
                word, emotion = clear_line.split(':')
                word = word.strip()
                if word in final_words:
                    emotion_list.append(emotion.strip())
except FileNotFoundError:
    print("The emotions.txt file is missing.")

# Counting the emotions
emotion_count = Counter(emotion_list)
print("Emotion Count:", emotion_count)

# Sentiment Analysis using VADER
def sentiment_analyse(sentiment_text):
    sia = SentimentIntensityAnalyzer()
    score = sia.polarity_scores(sentiment_text)
    print("Sentiment Score:", score)
    if score['neg'] > score['pos']:
        print("Negative Sentiment")
    elif score['neg'] < score['pos']:
        print("Positive Sentiment")
    else:
        print("Neutral Sentiment")

sentiment_analyse(cleaned_text)

# Plotting the emotions
if emotion_count:
    fig, ax1 = plt.subplots()
    ax1.bar(emotion_count.keys(), emotion_count.values())
    fig.autofmt_xdate()
    plt.savefig('graph.png')
    plt.show()
else:
    print("No emotions found in the text.")
