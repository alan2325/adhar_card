from django.shortcuts import render,HttpResponse

# Create your views here.
from flask import Flask, request, render_template
import pytesseract
from PIL import Image
import re
import os
# import pytesseract
from PIL import Image
from PIL import Image
# import pytesseract

# Path to Tesseract executable (update as needed)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Provide the correct file path
image_path = r'C:\Users\alankumar\Pictures\test_image.png'

# Check if the file exists
try:
    text = pytesseract.image_to_string(Image.open(image_path))
    print("Extracted Text:", text)
except FileNotFoundError:
    print(f"File not found: {image_path}")
except Exception as e:
    print(f"An error occurred: {e}")


app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return "No file uploaded.", 400

    file = request.files['image']
    if file.filename == '':
        return "No selected file.", 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    try:
        # Extract text from image
        text = pytesseract.image_to_string(Image.open(filepath))

        # Find Aadhaar number using regex
        aadhaar_number = re.search(r'\b\d{4}\s\d{4}\s\d{4}\b', text)
        if aadhaar_number:
            result = aadhaar_number.group(0)
        else:
            result = "No Aadhaar number found."

        # Clean up uploaded file
        os.remove(filepath)
    except Exception as e:
        result = f"Error processing image: {e}"

    return f"<h3>{result}</h3>"

if __name__ == '__main__':
    app.run(debug=True)
