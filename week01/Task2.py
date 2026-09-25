import numpy as np

# Create synthetic 300x400x3 matrix initialized with zeros
h, w, c = 300, 400, 3
image = np.zeros((h, w, c), dtype=np.uint8)

mid_h, mid_w = h // 2, w // 2

# Fill quadrants via spatial array slicing
image[0:mid_h, 0:mid_w] = [255, 0, 0]        # Top-Left: Pure Red
image[0:mid_h, mid_w:w] = [0, 255, 0]        # Top-Right: Pure Green
image[mid_h:h, 0:mid_w] = [0, 0, 255]        # Bottom-Left: Pure Blue
image[mid_h:h, mid_w:w] = [255, 255, 255]    # Bottom-Right: White

print("--- SYNTHETIC MATRIX METRICS ---")
print(f"Array Shape (H, W, C): {image.shape}")
print(f"Data Type: {image.dtype}")
print(f"Total Elements: {image.size:,} values")
print(f"Memory Footprint: {image.nbytes:,} bytes ({image.nbytes / 1024:.2f} KB)")
