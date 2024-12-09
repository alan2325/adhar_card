import pytesseract
from PIL import Image
import re

# Set the Tesseract-OCR executable path (adjust for your system)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Open the image file
image = Image.open("d:/aiswarya/adhar_card/card/aadhaar.png")

# Perform OCR on the image
text = pytesseract.image_to_string(image)

# Display the extracted text
print("Extracted Text:\n", text)

# Use regex to find 12-digit numbers (allowing spaces between digit groups)
pattern = r'\b(?:\d\s?){12}\b'
matches = re.findall(pattern, text)

# Clean up matches to remove spaces
matches = [''.join(re.findall(r'\d', match)) for match in matches]

# Display the found 12-digit numbers
if matches:
    print("\Aadhaar card number(s) found:")
    for match in matches:
        print(match)
else:
    print("\nAadhaar card numbers not found in the image.")
