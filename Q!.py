import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the grayscale image
image = cv2.imread('Input/tree.webp', cv2.IMREAD_GRAYSCALE)

# Check if image is loaded
if image is None:
    print("Error: Could not load image.")
    exit()

# User input
levels = int(input("Enter desired intensity levels (e.g., 2, 4, 8, 16, 32, 64, 128, 256): "))

# Validate input
if levels not in [2, 4, 8, 16, 32, 64, 128, 256]:
    print("Error: Please enter a valid power of 2 between 2 and 256.")
    exit()

# Reduce intensity levels
factor = 256 // levels
reduced_img = (image // factor) * factor

# Save result to file
cv2.imwrite('output/reduced_levels.png', reduced_img)
print(f"Reduced image saved to 'output/reduced_levels.png'.")

# Show with matplotlib instead of cv2.imshow
plt.imshow(reduced_img, cmap='gray')
plt.title(f'Reduced to {levels} Levels')
plt.axis('off')
plt.show()

