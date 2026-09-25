import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Load sample image
img = Image.open('sample.jpg')
img_arr = np.array(img)

# 1. Extract 2D intensity grids (Axis 2 slicing)
red_2d = img_arr[:, :, 0]
green_2d = img_arr[:, :, 1]
blue_2d = img_arr[:, :, 2]

print("--- CHANNEL EXTRACTION SUMMARY ---")
print(f"Original Image Shape: {img_arr.shape}")
print(f"Red Channel 2D Shape:   {red_2d.shape} | Mean Intensity: {red_2d.mean():.2f}")
print(f"Green Channel 2D Shape: {green_2d.shape} | Mean Intensity: {green_2d.mean():.2f}")
print(f"Blue Channel 2D Shape:  {blue_2d.shape} | Mean Intensity: {blue_2d.mean():.2f}")

# 2. Construct 3D single-channel isolation arrays
red_isolated = np.zeros_like(img_arr)
red_isolated[:, :, 0] = red_2d

green_isolated = np.zeros_like(img_arr)
green_isolated[:, :, 1] = green_2d

blue_isolated = np.zeros_like(img_arr)
blue_isolated[:, :, 2] = blue_2d

# 3. Render 2x3 subplot layout
fig, axes = plt.subplots(2, 3, figsize=(12, 7))

# Row 1: Isolated 3D Color Images
axes[0, 0].imshow(red_isolated)
axes[0, 0].set_title("Red Isolated View")
axes[0, 1].imshow(green_isolated)
axes[0, 1].set_title("Green Isolated View")
axes[0, 2].imshow(blue_isolated)
axes[0, 2].set_title("Blue Isolated View")

# Row 2: Grayscale 2D Intensity Grids
axes[1, 0].imshow(red_2d, cmap='gray')
axes[1, 0].set_title("Red Grayscale Map")
axes[1, 1].imshow(green_2d, cmap='gray')
axes[1, 1].set_title("Green Grayscale Map")
axes[1, 2].imshow(blue_2d, cmap='gray')
axes[1, 2].set_title("Blue Grayscale Map")

for ax in axes.flat:
    ax.axis('off')

plt.tight_layout()
plt.show()
