import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


# Load the image and convert to grayscale
image_path = "dog.jpg"  # Change to your image path
im = np.array(Image.open(image_path).convert('L'))

# Generate Gaussian noise
mean = 0
std = 60  # Standard deviation of noise
noise = np.random.normal(mean, std, im.shape)  # Create noise array

# Add noise to the image
noisy_im = im + noise

# Clip pixel values to stay in valid range [0, 255]
noisy_im = np.clip(noisy_im, 0, 255).astype(np.uint8)


# Display the original and noisy images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(im, cmap='gray')
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(noisy_im, cmap='gray')
plt.title("Noisy Image (Gaussian Noise)")
plt.axis("off")


plt.show()
