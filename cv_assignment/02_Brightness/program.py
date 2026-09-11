import cv2
import numpy as np
# Read the dark input image
img = cv2.imread("input.png")

if img is None:
    raise FileNotFoundError("input.png not found in the current folder.")
BRIGHTNESS_INCREASE = 80
sample_y, sample_x = img.shape[0] // 2, img.shape[1] // 2
pixel_before = img[sample_y, sample_x].copy()
bright = img.astype(np.int16) + BRIGHTNESS_INCREASE
bright = np.clip(bright, 0, 255).astype(np.uint8)

pixel_after = bright[sample_y, sample_x]

print(f"Sample pixel at ({sample_y}, {sample_x})")
print("Before brightness enhancement (B, G, R):", pixel_before)
print("After  brightness enhancement (B, G, R):", pixel_after)
cv2.imwrite("output.png", bright)
print("Saved brightness-enhanced output to output.png")
