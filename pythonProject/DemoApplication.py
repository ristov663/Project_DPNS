import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import cv2
import numpy as np
from PIL import ImageTk, Image

# Function to apply Canny edge detection
def apply_canny_edge_detection(image):
    # Conversion to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Applying Gaussian blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Applying Canny edge detection
    edges = cv2.Canny(blurred, 50, 150)

    return edges

# Function to apply Sobel edge detection
def apply_sobel_edge_detection(image):
    # Conversion to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Applying Sobel edge detection
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    edges = cv2.magnitude(sobelx, sobely)

    return edges

# Function to apply Prewitt edge detection
def apply_prewitt_edge_detection(image):
    # Conversion to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Applying Prewitt edge detection
    kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
    kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    img_prewittx = cv2.filter2D(gray, -1, kernelx)
    img_prewitty = cv2.filter2D(gray, -1, kernely)
    edges = cv2.addWeighted(img_prewittx, 0.5, img_prewitty, 0.5, 0)

    return edges

# Function to apply Roberts Cross edge detection
def apply_roberts_cross_edge_detection(image):
    # Conversion to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Applying Roberts Cross edge detection
    roberts_cross_v = np.array([[1, 0], [0, -1]])
    roberts_cross_h = np.array([[0, 1], [-1, 0]])
    vertical = cv2.filter2D(gray, -1, roberts_cross_v)
    horizontal = cv2.filter2D(gray, -1, roberts_cross_h)
    edges = np.sqrt(np.square(horizontal) + np.square(vertical))

    return edges

# Function to handle the Next button click event
def next_button_clicked():
    # Hide the current frame
    welcome_frame.pack_forget()

    # Show the algorithm selection frame
    algorithm_frame.pack()

# Function to handle the Apply button click event
def apply_button_clicked():
    # Get the selected algorithm
    selected_algorithm = algorithm_var.get()

    # Apply the selected algorithm to the image
    if selected_algorithm == "Canny Operator":
        edges = apply_canny_edge_detection(image)
    elif selected_algorithm == "Sobel Operator":
        edges = apply_sobel_edge_detection(image)
    elif selected_algorithm == "Prewitt Operator":
        edges = apply_prewitt_edge_detection(image)
    elif selected_algorithm == "Roberts Cross Operator":
        edges = apply_roberts_cross_edge_detection(image)

    # Display the edges image
    edges_img = Image.fromarray(edges)
    edges_img_tk = ImageTk.PhotoImage(edges_img)
    output_label.configure(image=edges_img_tk)
    output_label.image = edges_img_tk

# Function to handle the Save button click event
def save_button_clicked():
    # Open a file dialog to save the processed image
    file_path = filedialog.asksaveasfilename(defaultextension=".jpg")
    if file_path:
        # Save the processed image
        cv2.imwrite(file_path, edges)
        messagebox.showinfo("Save", "Image saved successfully!")

# Create the main window
window = tk.Tk()
window.title("ДЕМО АПЛИКАЦИЈА ЗА ДЕТЕКЦИЈА НА РАБОВИ")

# Create the welcome frame
welcome_frame = tk.Frame(window)
welcome_frame.pack(pady=20)

# Create the welcome label
welcome_label = tk.Label(welcome_frame, text="Демо апликација за детекција на рабови", font=("Arial", 18))
welcome_label.pack(pady=10)

# Create the file selection button
def select_image():
    file_path = filedialog.askopenfilename(initialdir='.', title='Select an Image')
    if file_path:
        global image, edges
        image = cv2.imread(file_path)
        edges = None
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (400, 300))
        image_pil = Image.fromarray(image)
        image_tk = ImageTk.PhotoImage(image_pil)
        input_label.configure(image=image_tk)
        input_label.image = image_tk

file_select_button = tk.Button(welcome_frame, text="Избери слика", command=select_image)
file_select_button.pack(pady=10)

# Create the next button
next_button = tk.Button(welcome_frame, text="Продолжи", command=next_button_clicked)
next_button.pack(pady=10)

# Create the algorithm selection frame
algorithm_frame = tk.Frame(window)

# Create the algorithm selection label
algorithm_label = tk.Label(algorithm_frame, text="Избери некој од наведените алгоритми!", font=("Arial", 18))
algorithm_label.pack(pady=10)

# Create the algorithm selection buttons
algorithm_var = tk.StringVar()
algorithm_var.set("Canny Operator")

canny_button = tk.Radiobutton(algorithm_frame, text="Canny алгоритам", variable=algorithm_var, value="Canny Operator")
canny_button.pack()

sobel_button = tk.Radiobutton(algorithm_frame, text="Sobel алгоритам", variable=algorithm_var, value="Sobel Operator")
sobel_button.pack()

prewitt_button = tk.Radiobutton(algorithm_frame, text="Prewitt алгоритам", variable=algorithm_var, value="Prewitt Operator")
prewitt_button.pack()

roberts_button = tk.Radiobutton(algorithm_frame, text="Roberts Cross алгоритам", variable=algorithm_var, value="Roberts Cross Operator")
roberts_button.pack()

# Create the apply button
apply_button = tk.Button(algorithm_frame, text="Примени алгоритам", command=apply_button_clicked)
apply_button.pack(pady=10)

# Create the input image label
input_label = tk.Label(algorithm_frame)
input_label.pack()

# Create the output image label
output_label = tk.Label(algorithm_frame)
output_label.pack()

# Create the save button
save_button = tk.Button(algorithm_frame, text="Зачувај", command=save_button_clicked)
save_button.pack(pady=10)

# Pack the algorithm frame initially (hidden)
algorithm_frame.pack_forget()

# Start the main loop
window.mainloop()
