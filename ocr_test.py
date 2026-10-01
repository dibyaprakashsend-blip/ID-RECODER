import pytesseract
from PIL import Image
import re

# Tell pytesseract where Tesseract is installed
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Open ID card
image = Image.open("my_id.jpeg")

# OCR
text = pytesseract.image_to_string(image)

print("========== OCR RESULT ==========")
print(text)
print("================================")

# Extract information from your ID card

name = re.search(
    r"\bDIBYA PRAKASH SEND\b",
    text,
    re.IGNORECASE
)

regd_no = re.search(
    r"Regd\.?\s*No\.?\s*:\s*([0-9]+)",
    text,
    re.IGNORECASE
)

course = re.search(
    r"Course\s*:\s*(.*)",
    text,
    re.IGNORECASE
)

abc_id = re.search(
    r"ABC\s*ID\s*:\s*([0-9]+)",
    text,
    re.IGNORECASE
)


# Get values

if name:
    name = name.group(0).strip()
else:
    name = None

if regd_no:
    regd_no = regd_no.group(1).strip()
else:
    regd_no = None

if course:
    course = course.group(1).strip()
else:
    course = None

if abc_id:
    abc_id = abc_id.group(1).strip()
else:
    abc_id = None


# Display

print("\n========== EXTRACTED DATA ==========")

print("Name       :", name)
print("Regd. No.  :", regd_no)
print("Course     :", course)
print("ABC ID     :", abc_id)