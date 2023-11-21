import seaborn as sns
import matplotlib.pyplot as plt
import sys
import pandas as pd
import os

# Extract command line arguments
Excellent = int(sys.argv[1])
Fine = int(sys.argv[2])
Moderate = int(sys.argv[3])
poorCount = int(sys.argv[4])
veryPoorCount = int(sys.argv[5])
Severe = int(sys.argv[6])
stationName = sys.argv[7]

# Create a dictionary with data
data = {
    'Категорія': ['Чудово', 'Добрий', 'Помірний', 'Шкідливий', 'Дуже\n шкідливий', 'Дуже\n тяжкий'],
    'Кількість': [Excellent, Fine, Moderate, poorCount, veryPoorCount, Severe]
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

plt.figure(figsize=(10, 6))

# Plot the bar plot using Seaborn
sns.barplot(x='Категорія', y='Кількість', data=df)

# Set plot title and labels
plt.title(f'Категорії оптимальних значень та кількість вимірювань середньодобових значень діокисду сірки (SO2),\n що відповідають категоріям на станції {stationName}')
plt.xlabel('Категорія якості повітря')
plt.ylabel('Кількість')

# Specify the file path
filename = "C:\\Users\\TheFelepOwl\\Documents\\nubip\\Tech_DataBase\\DataBase_visualizer\\grafix.png"

# Check if the file already exists and remove it
if os.path.exists(filename):
    os.remove(filename)

# Save the plot as an image file
plt.savefig(filename)


