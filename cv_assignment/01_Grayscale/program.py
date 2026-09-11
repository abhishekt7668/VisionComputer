import cv2
img = cv2.imread("input.png")

if img is None:
    raise FileNotFoundError("input.png not found in the current folder.")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
height, width = gray.shape
print("Original image shape (H, W, Channels):", img.shape)
print("Grayscale image shape (H, W):", gray.shape)
print("Height:", height)
print("Width:", width)
cv2.imwrite("output.png", gray)
print("Saved grayscale output to output.png")
