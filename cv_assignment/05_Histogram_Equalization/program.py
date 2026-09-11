

import cv2
import numpy as np
import matplotlib.pyplot as plt

gray = cv2.imread("input.png", cv2.IMREAD_GRAYSCALE)

if gray is None:
    raise FileNotFoundError("input.png not found in the current folder.")

equalized = cv2.equalizeHist(gray)
cv2.imwrite("output.png", equalized)
hist_before = cv2.calcHist([gray], [0], None, [256], [0, 256]).flatten()
hist_after = cv2.calcHist([equalized], [0], None, [256], [0, 256]).flatten()

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].plot(hist_before, color="blue")
axes[0].set_title("Histogram Before Equalization")
axes[0].set_xlabel("Pixel Intensity")
axes[0].set_ylabel("Frequency")

axes[1].plot(hist_after, color="green")
axes[1].set_title("Histogram After Equalization")
axes[1].set_xlabel("Pixel Intensity")
axes[1].set_ylabel("Frequency")

plt.tight_layout()
plt.savefig("histogram_comparison.png", bbox_inches="tight")
plt.close()
print("Saved comparison histogram to histogram_comparison.png")
