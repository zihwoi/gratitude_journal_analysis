import pandas as pd
import os
from collections import Counter
from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

# Ensure NLTK dependencies are downloaded
nltk.download('punkt_tab')
nltk.download('stopwords')

# Load dataset
csv_file_path = os.path.join('..', 'data', 'gratitude_entries.csv')
data = pd.read_csv(csv_file_path)

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

# Get words and counts for plotting
words, counts = zip(*top_words)

# Create a horizontal bar chart
plt.figure(figsize=(10, 6))
plt.barh(words, counts, color='skyblue')  # Use horizontal bars
plt.title('Top 10 Most Common Words in Gratitude Entries')
plt.xlabel('Frequency')
plt.ylabel('Words')
plt.xticks(rotation=45)

# Add value labels on the bars
for i, count in enumerate(counts):
    plt.text(count, i, str(count), ha='left', va='center')

plt.tight_layout()  # Adjust layout to prevent clipping of tick-labels
plt.show()
