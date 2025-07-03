from PIL import Image
import pytesseract

# If you're on Windows, specify the path like this:
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load the image from file
image = Image.open('3.png')

# Use pytesseract to extract text
text = pytesseract.image_to_string(image)

print("Extracted Text:")
print(text)
