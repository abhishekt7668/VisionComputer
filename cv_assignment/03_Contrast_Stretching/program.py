import cv2
import numpy as np
gray = cv2.imread("input.png", cv2.IMREAD_GRAYSCALE)

if gray is None:
    raise FileNotFoundError("input.png not found in the current folder.")
min_val = np.min(gray)
max_val = np.max(gray)
print("Minimum intensity value:", min_val)
print("Maximum intensity value:", max_val)

gray_float = gray.astype(np.float32)

if max_val == min_val:
    stretched = gray_float
else:
    stretched = (gray_float - min_val) * (255.0 / (max_val - min_val))

stretched = np.clip(stretched, 0, 255).astype(np.uint8)

print("New minimum after stretching:", np.min(stretched))
print("New maximum after stretching:", np.max(stretched))

cv2.imwrite("output.png", stretched)

print("Saved contrast-stretched output to output.png")


