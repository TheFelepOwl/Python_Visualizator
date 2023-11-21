import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import sys
import os

# Set up the Agg backend for matplotlib
import matplotlib
matplotlib.use('Agg')

# Extract command line arguments
poor_count = int(sys.argv[1])
very_poor_count = int(sys.argv[2])
station_name = sys.argv[3]

# Create a dictionary with data
data = {'Count': [poor_count, very_poor_count], 'Категорія': ['Шкідливий', 'Дуже тяжкий']}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Plot the bar plot using Seaborn
sns.barplot(x='Категорія', y='Count', data=df)

# Set plot title and labels
plt.title(f'Кількість середньодобових значень твердих частинок PM2.5 що відносяться до шкідливого рівню на станції {station_name}')
plt.xlabel('Категорія якості повітря')
plt.ylabel('Кількість')

filename = "C:\\Users\\TheFelepOwl\\Documents\\nubip\\Tech_DataBase\\DataBase_visualizer\\grafix.png"

# Save the plot as an image file
plt.savefig(filename)

# Display the plot (if needed)
plt.show()
