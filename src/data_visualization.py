import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('gratitude_entries.csv')

# Count entries by date
entries_by_date = df['Date'].value_counts().sort_index()

# Plotting
plt.figure(figsize=(10, 5))
entries_by_date.plot(kind='bar')
plt.title('Number of Gratitude Entries by Date')
plt.xlabel('Date')
plt.ylabel('Number of Entries')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('gratitude_entries_by_date.png')
plt.show()
