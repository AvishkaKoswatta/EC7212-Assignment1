import cv2
import matplotlib.pyplot as plt

#Input the original image 
image = cv2.imread('Input/tree.webp', cv2.IMREAD_COLOR)

if image is None:
    print("Error: Could not load image.")
    exit()

#spatial averaging
blur_3 = cv2.blur(image, (3, 3))
blur_10 = cv2.blur(image, (10, 10))
blur_20 = cv2.blur(image, (20, 20))


cv2.imwrite('Output/Q2/tree_blur_3x3_color.png', blur_3)
cv2.imwrite('Output/Q2/tree_blur_10x10_color.png', blur_10)
cv2.imwrite('Output/Q2/tree_blur_20x20_color.png', blur_20)

# # Display results using matplotlib (RGB format for correct color)
# titles = ['Original', '3x3 Averaging', '10x10 Averaging', '20x20 Averaging']
# images = [image, blur_3, blur_10, blur_20]

# plt.figure(figsize=(12, 5))
# for i in range(4):
#     plt.subplot(1, 4, i + 1)
#     # Convert BGR to RGB for matplotlib display
#     plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
#     plt.title(titles[i])
#     plt.axis('off')

# plt.tight_layout()
# plt.show()
