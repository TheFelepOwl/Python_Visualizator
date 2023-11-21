# show_plot.py
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Specify the path to the grafix.png file
filename = "C:\\Users\\TheFelepOwl\\Documents\\nubip\\Tech_DataBase\\DataBase_visualizer\\grafix.png"

# Display the image using matplotlib
img = mpimg.imread(filename)
imgplot = plt.imshow(img)

# Hide the axes
plt.axis('off')

# Show the image
plt.show()
