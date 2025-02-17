import cv2
import numpy as np

# Load the images
image_filenames = ['IMG1.jpg', 'IMG2.jpg', 'IMG3.jpg', 'IMG4.jpg', 'IMG5.jpg']
for filename in image_filenames:
    # Read the image
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

    # Apply Sobel operator
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)  # Sobel operator in X direction
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)  # Sobel operator in Y direction

    # Calculate gradient magnitude and direction
    gradient_magnitude = np.sqrt(sobelx ** 2 + sobely ** 2)
    gradient_direction = np.arctan2(sobely, sobelx)

    # Normalize gradient magnitude to 0-255 range
    gradient_magnitude = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

    # Threshold the gradient magnitude to obtain the binary edge map
    threshold_value = 50  # Adjust this threshold value as needed
    _, edge_map = cv2.threshold(gradient_magnitude, threshold_value, 255, cv2.THRESH_BINARY)

    # Display the resulting edge map
    cv2.imshow('Edge Map', edge_map)

    # Wait for a key press and then close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
