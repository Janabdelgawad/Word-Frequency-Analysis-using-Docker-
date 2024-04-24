import re
from collections import Counter
import nltk
from nltk.corpus import stopwords

# Download NLTK stopwords (if not already downloaded)
nltk.download("stopwords")

# Read the contents of the "random_paragraphs.txt" file
with open("random_paragraphs.txt", "r") as file:
    text = file.read()

# Remove punctuation and split the text into words
words = re.findall(r'\b\w+\b', text.lower())

# Remove NLTK stopwords
filtered_words = [word for word in words if word not in stopwords.words("english")]

# Count the frequency of each word
word_counts = Counter(filtered_words)

# Display word frequency count
for word, count in word_counts.items():
    print(f"{word}: {count}")
