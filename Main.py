import cv2
import numpy as np

def detect_defects(image_path):
    # Load the image
    image = cv2.imread("fruits_image.jpg")
    original = image.copy()
    cv2.imshow("Original Image", image)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply adaptive thresholding
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    cv2.imshow("Thresholded Image", thresh)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Calculate area and filter out small contours
        area = cv2.contourArea(contour)
        if area > 500:
            # Draw contour on the original image
            cv2.drawContours(original, [contour], -1, (0, 0, 255), 2)

            # Get bounding box for the contour
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(original, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Defects Detected", original)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
detect_defects("fruits_image.jpg")
