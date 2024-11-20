import cv2
import numpy as np

# Load the image
image = cv2.imread('apple.jpg')

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Otsu's thresholding
_, thresholded = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Display the original image
cv2.imshow('Original Image', image)

# Display the thresholded image
cv2.imshow('Thresholded Image', thresholded)

# Basic cleaning: Erosion and Dilation
erosion = cv2.erode(thresholded, None, iterations=1)
dilation = cv2.dilate(erosion, None, iterations=1)

# Display the cleaned images
cv2.imshow('Eroded Image', erosion)
cv2.imshow('Dilated Image', dilation)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
