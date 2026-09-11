import cv2
img = cv2.imread("input.png")

if img is None:
    raise FileNotFoundError("input.jpg not found in the current folder.")

kernel_size = (5, 5)
sigma = 0  

smoothed = cv2.GaussianBlur(img, kernel_size, sigma)
print(f"Applied Gaussian blur with kernel size {kernel_size}")

cv2.imwrite("output.png", smoothed)
print("Saved Gaussian-smoothed output to output.png")
