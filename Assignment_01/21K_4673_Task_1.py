# from PIL import Image
# from pylab import *
# # read image to array
# im = array(Image.open('/workspaces/Computer-Vision-Practice/Assignment_01/shelf.jpg'))
# # plot the image
# imshow(im)
# # some points
# x = [100,100,400,400]
# y = [200,500,200,500]
# # plot the points with red star-markers
# plot(x,y,'r*')
# # line plot connecting the first two points
# plot(x[:2],y[:2])
# # add title and show the plot
# title('Plotting: "/workspaces/Computer-Vision-Practice/Assignment_01/shelf.jpg"')
# show()

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Load image
image_path = "/workspaces/Computer-Vision-Practice/Assignment_01/shelf.jpg"
im = np.array(Image.open(image_path))

# Create figure and display image
plt.figure(figsize=(8, 6))
plt.imshow(im)

# Define some points
x = [100, 100, 400, 400]
y = [200, 500, 200, 500]

# Plot the points with red star markers
plt.plot(x, y, 'r*', markersize=10, label="Points")

# Line plot connecting the first two points
plt.plot(x[:2], y[:2], 'b-', linewidth=2, label="Line")

# Add title and legend
plt.title(f'Plotting: "{image_path}"')
plt.legend()

# Show the plot
plt.show()
