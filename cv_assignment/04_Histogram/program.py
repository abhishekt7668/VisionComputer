import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the input image as grayscale
gray = cv2.imread("input.png", cv2.IMREAD_GRAYSCALE)

if gray is None:
    raise FileNotFoundError("input.jpg not found in the current folder.")

# Compute the histogram (256 bins for intensities 0-255)
hist = cv2.calcHist([gray], [0], None, [256], [0, 256]).flatten()

# Intensity value with the highest frequency (the mode)
peak_intensity = int(np.argmax(hist))
peak_frequency = int(hist[peak_intensity])
print("Intensity value with highest frequency:", peak_intensity)
print("Frequency at that intensity:", peak_frequency)

# Plot the histogram
plt.figure(figsize=(8, 5))
plt.plot(hist, color="black")
plt.title("Grayscale Intensity Histogram")
plt.xlabel("Pixel Intensity (0-255)")
plt.ylabel("Frequency")
plt.axvline(peak_intensity, color="red", linestyle="--",
            label=f"Peak = {peak_intensity}")
plt.legend()
plt.tight_layout()

plt.savefig("output.png", bbox_inches="tight")
plt.close()
print("Saved histogram plot to output.png")

