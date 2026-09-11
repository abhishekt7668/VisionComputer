import cv2
img = cv2.imread("input.png")

if img is None:
    raise FileNotFoundError("input.png not found in the current folder.")

kernel_size = 5
filtered = cv2.medianBlur(img, kernel_size)

print(f"Applied median filter with kernel size {kernel_size}")
cv2.imwrite("output.png", filtered)
print("Saved median-filtered output to output.png")
