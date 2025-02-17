import numpy as np
from PIL import Image
import cv2

# List of image filenames
image_files = ["IMG1.jpg", "IMG2.jpg"]

# Loop through the image files
for image_file in image_files:
    # Open the image
    img = np.array(Image.open(image_file)).astype(np.uint8)

    # Apply gray scale
    gray_img = np.round(0.299 * img[:, :, 0] +
                        0.587 * img[:, :, 1] +
                        0.114 * img[:, :, 2]).astype(np.uint8)

    # Prewitt Operator
    h, w = gray_img.shape
    # define filters
    horizontal = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])  # s2
    vertical = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])  # s1

    # define images with 0s
    newgradientImage = np.zeros((h - 2, w - 2))

    # offset by 1
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            horizontalGrad = (horizontal[0, 0] * gray_img[i - 1, j - 1]) + \
                             (horizontal[0, 1] * gray_img[i - 1, j]) + \
                             (horizontal[0, 2] * gray_img[i - 1, j + 1]) + \
                             (horizontal[1, 0] * gray_img[i, j - 1]) + \
                             (horizontal[1, 1] * gray_img[i, j]) + \
                             (horizontal[1, 2] * gray_img[i, j + 1]) + \
                             (horizontal[2, 0] * gray_img[i + 1, j - 1]) + \
                             (horizontal[2, 1] * gray_img[i + 1, j]) + \
                             (horizontal[2, 2] * gray_img[i + 1, j + 1])

            verticalGrad = (vertical[0, 0] * gray_img[i - 1, j - 1]) + \
                           (vertical[0, 1] * gray_img[i - 1, j]) + \
                           (vertical[0, 2] * gray_img[i - 1, j + 1]) + \
                           (vertical[1, 0] * gray_img[i, j - 1]) + \
                           (vertical[1, 1] * gray_img[i, j]) + \
                           (vertical[1, 2] * gray_img[i, j + 1]) + \
                           (vertical[2, 0] * gray_img[i + 1, j - 1]) + \
                           (vertical[2, 1] * gray_img[i + 1, j]) + \
                           (vertical[2, 2] * gray_img[i + 1, j + 1])

            # Edge Magnitude
            mag = np.sqrt(pow(horizontalGrad, 2.0) + pow(verticalGrad, 2.0))
            newgradientImage[i - 1, j - 1] = mag

    # Convert the image to uint8 and scale the values to 0-255
    newgradientImage = (255 * (newgradientImage / np.max(newgradientImage))).astype(np.uint8)

    # Show the image using cv2.imshow
    cv2.imshow("Prewitt Edges", newgradientImage)
    cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()

