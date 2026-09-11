import cv2
import numpy as np
img = cv2.imread("input.png")

if img is None:
    raise FileNotFoundError("input.png not found in the current folder.")
smooth = cv2.GaussianBlur(img, (7, 7), 0)
cv2.imwrite("output_smooth.png", smooth)
print("Saved smoothed output to output_smooth.png")

sharpen_kernel = np.array([
    [ 0, -1,  0],
    [-1,  5, -1],
    [ 0, -1,  0]
], dtype=np.float32)

sharp = cv2.filter2D(img, -1, sharpen_kernel)
cv2.imwrite("output_sharp.png", sharp)
print("Saved sharpened output to output_sharp.png")

print("\nObservation: Smoothing reduces noise and detail by averaging")
print("neighboring pixels, while sharpening enhances edges/detail by")
print("emphasizing local intensity differences.")
