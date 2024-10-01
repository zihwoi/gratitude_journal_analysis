import pandas as pd
import os
from collections import Counter
from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from textblob import TextBlob

# Create a word cloud of the most common words
from wordcloud import WordCloud

# Ensure NLTK dependencies are downloaded
nltk.download('punkt_tab')
nltk.download('stopwords')

# Load dataset
csv_file_path = os.path.join('..', 'data', 'gratitude_entries.csv')
data = pd.read_csv(csv_file_path)

# Define the function to get sentiment
def get_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity, analysis.sentiment.subjectivity

# Tokenize words and remove punctuation and stop words
def clean_text(text):
    tokens = word_tokenize(text.lower())  # Convert to lowercase
    tokens = [word for word in tokens if word.isalnum()]  # Remove punctuation
    tokens = [word for word in tokens if word not in stopwords.words('english')]  # Remove stop words
    return tokens

# Apply cleaning function to the 'Gratitude' column
data['Tokens'] = data['Gratitude'].apply(clean_text)

# Create word frequency counts
all_words = [word for tokens in data['Tokens'] for word in tokens]
word_freq = Counter(all_words)

# Print the top 10 most common words
print("Top 10 Most Common Words in Gratitude Entries:")
top_words = word_freq.most_common(10)
for word, freq in top_words:
    print(f"{word}: {freq}")

# Save the word frequencies to a CSV file for later analysis
word_freq_df = pd.DataFrame(word_freq.items(), columns=['Word', 'Frequency'])
word_freq_df.to_csv(os.path.join('..', 'data', 'word_frequencies.csv'), index=False)

# Apply sentiment analysis
data[['Polarity', 'Subjectivity']] = data['Gratitude'].apply(lambda x: pd.Series(get_sentiment(x)))

# Print the first few rows to see the results
print(data[['Gratitude', 'Polarity', 'Subjectivity']].head())

# Create a bar chart for common words
words, counts = zip(*top_words)

plt.figure(figsize=(10, 6))
plt.bar(words, counts, color='skyblue')
plt.title('Top 10 Most Common Words in Gratitude Entries')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.show()


# Generate and display the word cloud
# Combine all words into a single string
all_text = ' '.join(all_words)

# Create a word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_text)

# Display the word cloud
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Hide axes
plt.title('Word Cloud of Most Common Words')
plt.show()