import cv2
import numpy as np
from scipy import ndimage
import os

# Path to the directory containing the images
image_dir = os.path.dirname(os.path.abspath(__file__))

# List of image filenames
image_files = ["IMG1.jpg", "IMG2.jpg", "IMG3.jpg", "IMG4.jpg", "IMG5.jpg"]

# Loop through the image files
for image_file in image_files:
    # Read the image
    image_path = os.path.join(image_dir, image_file)
    img = cv2.imread(image_path, 0).astype('float64')
    img /= 255.0

    # Apply the Roberts Cross Operator
    roberts_cross_v = np.array([[1, 0], [0, -1]])
    roberts_cross_h = np.array([[0, 1], [-1, 0]])
    vertical = ndimage.convolve(img, roberts_cross_v)
    horizontal = ndimage.convolve(img, roberts_cross_h)
    edged_img = np.sqrt(np.square(horizontal) + np.square(vertical))
    edged_img *= 255

    # Display the image

    cv2.imshow("Roberts Cross Edges", edged_img.astype(np.uint8))
    cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
