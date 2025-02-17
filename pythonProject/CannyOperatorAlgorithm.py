import cv2
import os

def apply_canny_edge_detection(image):
    # Conversion to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Applying Gaussian blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Applying Canny edge detection
    edges = cv2.Canny(blurred, 50, 150)

    return edges

# Get the file paths of the images
image_folder = '.'  # Current folder
image_files = ['IMG1.jpg', 'IMG2.jpg', 'IMG3.jpg', 'IMG4.jpg', 'IMG5.jpg']

# Process each image
for image_file in image_files:
    image_path = os.path.join(image_folder, image_file)

    # Read the image
    image = cv2.imread(image_path)

    # Apply Canny edge detection
    edges = apply_canny_edge_detection(image)

    # Display the edges image
    cv2.imshow('Edges', edges)

    # Wait for key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
