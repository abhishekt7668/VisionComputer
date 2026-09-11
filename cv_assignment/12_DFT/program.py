import cv2
import numpy as np
gray = cv2.imread("input.png", cv2.IMREAD_GRAYSCALE)

if gray is None:
    raise FileNotFoundError("input.jpg not found in the current folder.")

print("Original image shape:", gray.shape)
img_float32 = np.float32(gray)
dft = cv2.dft(img_float32, flags=cv2.DFT_COMPLEX_OUTPUT)
print("DFT result shape:", dft.shape)
dft_shifted = np.fft.fftshift(dft)
print("Shifted DFT result shape:", dft_shifted.shape)
magnitude = cv2.magnitude(dft_shifted[:, :, 0], dft_shifted[:, :, 1])
magnitude_log = 20 * np.log(magnitude + 1)  # +1 avoids log(0)
magnitude_norm = cv2.normalize(magnitude_log, None, 0, 255, cv2.NORM_MINMAX)
magnitude_norm = magnitude_norm.astype(np.uint8)

cv2.imwrite("output.png", magnitude_norm)
print("Saved DFT magnitude visualization to output.png")
