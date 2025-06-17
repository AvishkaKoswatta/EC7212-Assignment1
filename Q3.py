import cv2
import matplotlib.pyplot as plt

# Input the original 
image = cv2.imread('Input/tree.webp', cv2.IMREAD_COLOR)

if image is None:
    print("Error: Could not load image.")
    exit()

#Get image dimensions
(h, w) = image.shape[:2]
center = (w // 2, h // 2)

# Rotate 45 degrees
M_45 = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_45 = cv2.warpAffine(image, M_45, (w, h))  # May crop corners

# Rotate 90 degrees 
rotated_90 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite('Output/Q3/tree_rotated_45_color.png', rotated_45)
cv2.imwrite('Output/Q3/tree_rotated_90_color.png', rotated_90)

# # Display using matplotlib (BGR -> RGB)
# titles = ['Original', 'Rotated 45°', 'Rotated 90°']
# images = [image, rotated_45, rotated_90]

# plt.figure(figsize=(10, 4))
# for i in range(3):
#     plt.subplot(1, 3, i + 1)
#     plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
#     plt.title(titles[i])
#     plt.axis('off')

# plt.tight_layout()
# plt.show()
