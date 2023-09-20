import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import pytesseract
import PIL.Image

# Function to display the selected image
def display_image(file_path):
    global selected_image
    selected_image = file_path
    img = Image.open(selected_image)
    img.thumbnail((300, 300))  # Resize the image (adjust the size as needed)
    img = ImageTk.PhotoImage(img)
    image_label.config(image=img)
    image_label.image = img
    generate_button.config(state=tk.NORMAL)  # Enable the "Generate" button

# Function to update the displayed image
def update_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif *.bmp")])
    if file_path:
        display_image(file_path)

# Function to display "Done" and allow text selection
def display_text():
    config = r"--psm 11 --oem 3" 
    text = pytesseract.image_to_string(PIL.Image.open(selected_image), config=config)
    result_text.config(state=tk.NORMAL)  # Enable text insertion
    result_text.delete(1.0, tk.END)  # Clear any previous text
    result_text.insert(tk.END, text)
    result_text.see(tk.END)  # Scroll to the end to make the last line visible

# Create the main window
root = tk.Tk()
root.title("OCR GUI")

# Create and configure the labels
padding = tk.Label(root, text="")
result_text = tk.Text(root, wrap=tk.WORD, state=tk.DISABLED)  # Text field for "Done" text
result_text.tag_configure("center", justify="center")
result_text.insert(tk.END, "Done", "center")

# Create and configure the buttons
select_button = tk.Button(root, text="Select Image", command=update_image)
generate_button = tk.Button(root, text="Extract", command=display_text, state=tk.DISABLED)  # Initially disabled

# Create a label to display the selected image
image_label = tk.Label(root)

# Pack widgets
padding.pack(pady=20)
select_button.pack()
image_label.pack(pady=10)
generate_button.pack()
result_text.pack()

selected_image = None

# Start the tkinter main loop
root.mainloop()
