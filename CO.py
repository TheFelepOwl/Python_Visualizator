import seaborn as sns
import matplotlib.pyplot as plt
import sys
import pandas as pd
import os

# Extract command line arguments
Excellent = int(sys.argv[1])
Fine = int(sys.argv[2])
Moderate = int(sys.argv[3])
stationName = sys.argv[4]

# Create a dictionary with data
data = {
    'Категорія': ['Чудово', 'Добрий', 'Помірний'],
    'Кількість': [Excellent, Fine, Moderate]
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Plot the bar plot using Seaborn
sns.barplot(x='Категорія', y='Кількість', data=df)

# Set plot title and labels
plt.title(f'Якість повітря на станції {stationName}')
plt.xlabel('Категорія якості повітря')
plt.ylabel('Кількість')

# Specify the file path
filename = "C:\\Users\\TheFelepOwl\\Documents\\nubip\\Tech_DataBase\\DataBase_visualizer\\grafix.png"

# Check if the file already exists and remove it
if os.path.exists(filename):
    os.remove(filename)

# Save the plot as an image file
plt.savefig(filename)


