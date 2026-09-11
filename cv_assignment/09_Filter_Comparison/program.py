import cv2
img = cv2.imread("input.png")

if img is None:
    raise FileNotFoundError("input.jpg not found in the current folder.")

kernel_size = 5
mean_result = cv2.blur(img, (kernel_size, kernel_size))
cv2.imwrite("output_mean.png", mean_result)
print("Saved mean filter result to output_mean.png")
gaussian_result = cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)
cv2.imwrite("output_gaussian.png", gaussian_result)
print("Saved Gaussian filter result to output_gaussian.png")
median_result = cv2.medianBlur(img, kernel_size)
cv2.imwrite("output_median.png", median_result)
print("Saved median filter result to output_median.png")

print("\nObservation: Median filtering typically removes salt-and-pepper")
print("noise most effectively while preserving edges better than Mean")
print("or Gaussian filtering, which tend to blur edges along with noise.")
