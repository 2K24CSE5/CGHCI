import math

def calculate_display_metrics():
    print("--- DISPLAY METRICS ANALYSIS ---")
    w_px = int(input("Enter horizontal resolution (pixels): "))
    h_px = int(input("Enter vertical resolution (pixels): "))
    d_inches = float(input("Enter physical diagonal size (inches): "))

    # Total pixels
    total_pixels = w_px * h_px

    # Aspect ratio using greatest common divisor
    divisor = math.gcd(w_px, h_px)
    aspect_w = w_px // divisor
    aspect_h = h_px // divisor

    # PPI/DPI calculation
    diagonal_pixels = math.sqrt(w_px**2 + h_px**2)
    dpi = diagonal_pixels / d_inches

    # Classification
    if dpi < 100:
        category = "Low Density (Standard Monitor)"
    elif 100 <= dpi <= 200:
        category = "Medium Density (HD Display)"
    else:
        category = "High Density (Retina / Mobile)"

    print(f"\nTotal Pixel Count: {total_pixels:,} pixels")
    print(f"Aspect Ratio: {aspect_w}:{aspect_h}")
    print(f"Calculated DPI: {dpi:.2f} DPI")
    print(f"Density Category: {category}")

if __name__ == "__main__":
    calculate_display_metrics()
