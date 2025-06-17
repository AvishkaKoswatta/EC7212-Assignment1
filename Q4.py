import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('Input/tree.webp', cv2.IMREAD_COLOR)

if image is None:
    print("Error: Could not load image.")
    exit()

#apply block averaging
def block_average(img, block_size):
    h, w, c = img.shape
    out = img.copy()
    
    for y in range(0, h - block_size + 1, block_size):
        for x in range(0, w - block_size + 1, block_size):
            block = img[y:y + block_size, x:x + block_size]
            avg_color = block.mean(axis=(0, 1)).astype(np.uint8)
            out[y:y + block_size, x:x + block_size] = avg_color
    return out

# Apply block averaging for 3x3, 5x5, 7x7
avg_3x3 = block_average(image, 3)
avg_5x5 = block_average(image, 5)
avg_7x7 = block_average(image, 7)


cv2.imwrite('Output/Q4/tree_block_avg_3x3.png', avg_3x3)
cv2.imwrite('Output/Q4/tree_block_avg_5x5.png', avg_5x5)
cv2.imwrite('Output/Q4/tree_block_avg_7x7.png', avg_7x7)

# Display results
# titles = ['Original', '3x3 Block Avg', '5x5 Block Avg', '7x7 Block Avg']
# images = [image, avg_3x3, avg_5x5, avg_7x7]

# plt.figure(figsize=(12, 5))
# for i in range(4):
#     plt.subplot(1, 4, i + 1)
#     plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
#     plt.title(titles[i])
#     plt.axis('off')

# plt.tight_layout()
# plt.show()
