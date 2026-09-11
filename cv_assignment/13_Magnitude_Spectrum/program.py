import cv2
import numpy as np
gray = cv2.imread("input.png", cv2.IMREAD_GRAYSCALE)
if gray is None:
    raise FileNotFoundError("input.png not found in the current folder.")
img_float32 = np.float32(gray)
dft = cv2.dft(img_float32, flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shifted = np.fft.fftshift(dft)

magnitude = cv2.magnitude(dft_shifted[:, :, 0], dft_shifted[:, :, 1])
magnitude_spectrum = 20 * np.log(magnitude + 1)
magnitude_spectrum = cv2.normalize(magnitude_spectrum, None, 0, 255,
                                    cv2.NORM_MINMAX)
magnitude_spectrum = magnitude_spectrum.astype(np.uint8)
cv2.imwrite("output.png", magnitude_spectrum)
print("Saved magnitude spectrum to output.png")
