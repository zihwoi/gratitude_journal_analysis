import pandas as pd
from faker import Faker
import random
import os
from gratitude_phrases import positive_phrases, neutral_phrases, negative_phrases  # Import the phrases

# Initialize Faker
fake = Faker()

# Specify the data directory
data_directory = r'C:\Users\zihwoi\Documents\GitHub\gratitude_journal_analysis\data'
os.makedirs(data_directory, exist_ok=True)
    
# Generate synthetic gratitude entries
def generate_gratitude_entries(num_entries):
    data = {
        'Date': [],
        'Gratitude': [],
        'Sentiment': [],
        'Name': []
    }

    used_gratitudes = set()  # To keep track of used gratitude entries
    max_attempts = 1000  # Max attempts to find unique entries
    attempts = 0
    
    while len(data['Gratitude']) < num_entries:
        sentiment_type = random.choice(['positive', 'neutral', 'negative'])
        
        if sentiment_type == 'positive':
            gratitude_entry = random.choice(positive_phrases)
        elif sentiment_type == 'neutral':
            gratitude_entry = random.choice(neutral_phrases)
        else:
            gratitude_entry = random.choice(negative_phrases)

        # Only add unique gratitude entries
        if gratitude_entry not in used_gratitudes:
            used_gratitudes.add(gratitude_entry)
            data['Gratitude'].append(gratitude_entry)
            data['Date'].append(fake.date_this_year())  # Generate a random date
            data['Name'].append(fake.name())  # Generate a random name
            data['Sentiment'].append(sentiment_type)  # Record sentiment type
            
            # Check if you've reached the required number of entries
            if len(data['Gratitude']) >= num_entries:
                break

    return pd.DataFrame(data)

# Specify the number of entries to generate
num_entries = 250
data_directory = r'C:\Users\zihwoi\Documents\GitHub\gratitude_journal_analysis\data'

# Ensure the data directory exists
os.makedirs(data_directory, exist_ok=True)

# Generate a new filename based on existing files
base_filename = 'gratitude_entries'
file_extension = '.csv'
file_count = 0

# Find the next available filename
while True:
    if file_count == 0:
        csv_file_path = os.path.join(data_directory, f'{base_filename}{file_extension}')
    else:
        csv_file_path = os.path.join(data_directory, f'{base_filename}_{file_count}{file_extension}')
    
    if not os.path.exists(csv_file_path):
        break  # Found an available filename
    file_count += 1

# Generate new gratitude entries
new_gratitude_df = generate_gratitude_entries(num_entries)

# Save the new entries to the unique file
new_gratitude_df.to_csv(csv_file_path, index=False, encoding='utf-8-sig')
print(f'Generated {num_entries} gratitude entries and saved to {csv_file_path}.')
