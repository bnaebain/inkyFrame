import os
import time
from PIL import Image

import sys

sys.path.append("/home/brinae/inky/inky")

from inky.auto import auto

# Initialize Inky display
inky_display = auto()
inky_display.set_border(inky_display.WHITE)  # Adjust as needed

# Folder where images are stored
image_folder = "images"

# Get all images in the folder
def get_images():
    return sorted([f for f in os.listdir(image_folder) if f.endswith((".png", ".jpg", ".bmp"))])

# Function to display an image
def display_image(image_path):
    img = Image.open(image_path)
    img = img.resize(inky_display.resolution)  # Resize to fit screen
    inky_display.set_image(img)
    inky_display.show()

# Rotate through images
while True:
    images = get_images()
    if not images:
        print("No images found in folder.")
    else:
        for img in images:
            print(f"Displaying: {img}")
            display_image(os.path.join(image_folder, img))
            time.sleep(30)  # Change image every 30 seconds

