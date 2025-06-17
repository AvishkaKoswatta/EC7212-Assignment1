import cv2
import numpy as np
# import matplotlib.pyplot as plt

#Input the grayscale image
image = cv2.imread('Input/tree.webp', cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Could not load image.")
    exit()

#User enter input
levels = int(input("Enter desired intensity levels (e.g., 2, 4, 8, 16, 32, 64, 128, 256): "))

#Validating the input
if levels not in [2, 4, 8, 16, 32, 64, 128, 256]:
    print("Error: Please enter a valid power of 2 between 2 and 256.")
    exit()

#Reduce intensity levels
factor = 256 // levels
reduced_img = (image // factor) * factor


cv2.imwrite('Output/Q1/reduced_levels_256.png', reduced_img)
print(f"Reduced image saved to 'Output/reduced_levels.png'.")



