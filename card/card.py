import pytesseract
from PIL import Image
import os

# Set the correct path for Tesseract (adjust if necessary)
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'  # Update this for your system

# Get the image file path from the user
file_path = "/aadhaar.png"

# Check if the file exists
if os.path.exists(file_path):
    try:
        # Open the image and perform OCR
        img = Image.open(file_path)
        text = pytesseract.image_to_string(img)
        
        # Display the extracted text
        print("\nExtracted Text from Image:")
        print(text)
        
        # Extract the 12-digit code using regex
        import re
        pattern = r'\b\d{12}\b'
        matches = re.findall(pattern, text)
        
        if matches:
            print("\n12-digit code(s) found:")
            for match in matches:
                print(match)
        else:
            print("\nNo 12-digit code found.")
    except Exception as e:
        print(f"An error occurred while processing the image: {e}")
else:
    print("File not found! Please check the path and try again.")
