import cv2
img = cv2.imread("input.png")

if img is None:
    raise FileNotFoundError("input.png not found!")

mean_filtered = cv2.blur(img, (3, 3))

cv2.imwrite("output.png", mean_filtered)




