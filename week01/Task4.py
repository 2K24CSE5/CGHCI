import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img = Image.open('sample.jpg')
img_arr = np.array(img)

n = 8

# 1. Downsampling via slicing step
downsampled = img_arr[::n, ::n, :]

# 2. Re-expand back using np.repeat along vertical (0) and horizontal (1) axes
pixelated = np.repeat(np.repeat(downsampled, n, axis=0), n, axis=1)

# Handle possible edge alignment if dimensions aren't exact multiples of n
pixelated = pixelated[:img_arr.shape[0], :img_arr.shape[1], :]

# 3. Dimension & Memory Metrics
orig_bytes = img_arr.nbytes
down_bytes = downsampled.nbytes

dim_reduction = (1 - (downsampled.shape[0] / img_arr.shape[0])) * 100
mem_savings = (1 - (down_bytes / orig_bytes)) * 100

print(f"--- DOWNSAMPLING ANALYSIS (N={n}) ---")
print(f"Original Shape:     {img_arr.shape} | Memory: {orig_bytes:,} bytes")
print(f"Downsampled Shape:  {downsampled.shape}  | Memory: {down_bytes:,} bytes")
print(f"Re-expanded Shape:  {pixelated.shape} | Visual: Blocky Pixelation")
print(f"Dimension Reduction: {dim_reduction:.2f}% reduction per axis")
print(f"Memory Savings:      {mem_savings:.2f}% data reduction")

# Visual Display
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(img_arr)
axes[0].set_title("Original Image")
axes[0].axis('off')

axes[1].imshow(pixelated)
axes[1].set_title(f"Pixelated Image (N={n})")
axes[1].axis('off')

plt.tight_layout()
plt.show()
