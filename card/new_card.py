import pytesseract
from PIL import Image

# Set the correct path for Tesseract (adjust if necessary)
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# Open an image file
img = Image.open('/home/software-9am/Downloads/adhar.png')

# Use tesseract to do OCR on the image
text = pytesseract.image_to_string(img)

print(text)
