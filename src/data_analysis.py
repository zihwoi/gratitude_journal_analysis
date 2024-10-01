import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
import os

# Load the dataset
csv_file_path = os.path.join('..', 'data', 'gratitude_entries.csv')
data = pd.read_csv(csv_file_path)

# Basic statistics on sentiment
sentiment_counts = data['Sentiment'].value_counts()
sentiment_percentage = data['Sentiment'].value_counts(normalize=True) * 100

print("Sentiment Counts:")
print(sentiment_counts)
print("\nSentiment Percentage:")
print(sentiment_percentage)

# Convert 'Date' to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Group by month and count entries
monthly_trends = data.resample('ME', on='Date').count()

# Plotting the trend
plt.figure(figsize=(12, 6))
plt.plot(monthly_trends.index, monthly_trends['Gratitude'], marker='o')
plt.title('Monthly Gratitude Entries')
plt.xlabel('Date')
plt.ylabel('Number of Entries')
plt.grid()
plt.xticks(rotation=45)
plt.show()

# Function to get sentiment polarity
def analyze_sentiment(entry):
    return TextBlob(entry).sentiment.polarity

# Apply sentiment analysis to gratitude entries
data['Polarity'] = data['Gratitude'].apply(analyze_sentiment)

# Check correlation between sentiment and date
correlation = data[['Date', 'Polarity']].groupby('Date').mean().reset_index()
print(correlation)

# Optional: Visualize sentiment over time
plt.figure(figsize=(12, 6))
plt.plot(correlation['Date'], correlation['Polarity'], marker='o')
plt.title('Average Sentiment Polarity Over Time')
plt.xlabel('Date')
plt.ylabel('Average Polarity')
plt.grid()
plt.xticks(rotation=45)
plt.show()

sentiment_trends = data.groupby([pd.Grouper(key='Date', freq='ME'), 'Sentiment']).size().unstack().fillna(0)
sentiment_trends.plot(kind='line', stacked=True, figsize=(12, 6))
plt.title('Monthly Sentiment Breakdown')
plt.xlabel('Date')
plt.ylabel('Number of Entries')
plt.grid()
plt.xticks(rotation=45)
plt.show()
