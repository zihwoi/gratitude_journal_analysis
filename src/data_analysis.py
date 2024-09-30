import pandas as pd

# Load the data
df = pd.read_csv('gratitude_entries.csv')

# Display the first few rows of the data
print(df.head())

# Basic statistics
print(df.describe())

# Count entries by date
entries_by_date = df['Date'].value_counts()
print(entries_by_date)

# Save the analysis results if needed
entries_by_date.to_csv('entries_by_date.csv')
