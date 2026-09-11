import cv2
import numpy as np
img = cv2.imread("input.png")

if img is None:
    raise FileNotFoundError("input.jpg not found in the current folder.")

sharpen_kernel = np.array([
    [ 0, -1,  0],
    [-1,  5, -1],
    [ 0, -1,  0]
], dtype=np.float32)

sharpened = cv2.filter2D(img, -1, sharpen_kernel)
print("Applied custom sharpening kernel:\n", sharpen_kernel)
cv2.imwrite("output.png", sharpened)
print("Saved sharpened output to output.png")
