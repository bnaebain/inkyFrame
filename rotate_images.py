import os
import time
import random
from PIL import Image

import sys

sys.path.append("/home/brinae/inky/inky")

from inky import Inky7Colour as Inky

# Initialize Inky display
inky_display = Inky()
inky_display.set_border(inky_display.WHITE)  # Adjust as needed

# Folder where images are stored
image_folder = "images"

# Get all images in the folder and shuffle them
def get_images():
    images = [f for f in os.listdir(image_folder) if f.endswith((".png", ".jpg", ".bmp"))]
    random.shuffle(images)  # Shuffle the image list
    return images

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
            time.sleep(1800)  # Change image every 30 minutes
