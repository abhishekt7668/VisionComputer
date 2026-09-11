import cv2
import numpy as np
gray = cv2.imread("input.png", cv2.IMREAD_GRAYSCALE)

if gray is None:
    raise FileNotFoundError("input.png not found in the current folder.")

rows, cols = gray.shape
center_row, center_col = rows // 2, cols // 2
img_float32 = np.float32(gray)
dft = cv2.dft(img_float32, flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shifted = np.fft.fftshift(dft)
radius = 30
mask = np.ones((rows, cols, 2), dtype=np.float32)
y, x = np.ogrid[:rows, :cols]
distance = (x - center_col) ** 2 + (y - center_row) ** 2
mask_area = distance <= radius ** 2
mask[mask_area] = 0
filtered_dft = dft_shifted * mask
filtered_dft_unshifted = np.fft.ifftshift(filtered_dft)
img_reconstructed = cv2.idft(filtered_dft_unshifted)
img_reconstructed = cv2.magnitude(img_reconstructed[:, :, 0],
                                   img_reconstructed[:, :, 1])

img_reconstructed = cv2.normalize(img_reconstructed, None, 0, 255,
                                   cv2.NORM_MINMAX)
img_reconstructed = img_reconstructed.astype(np.uint8)
cv2.imwrite("output.png", img_reconstructed)
print(f"Applied high-pass filter with radius {radius}")
print("Saved HPF reconstructed output to output.png")
