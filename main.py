import pytesseract
from google.cloud import translate_v2 as translate
from google.cloud import speech
import boto3

# Cấu hình Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'/app/.apt/usr/bin/tesseract'

# Hàm nhận diện văn bản từ hình ảnh
def extract_text_from_image(image_path):
    text = pytesseract.image_to_string(image_path)
    return text

# Hàm dịch văn bản
def translate_text(text, target_language='vi'):
    translate_client = translate.Client()
    result = translate_client.translate(text, target_language=target_language)
    return result['translatedText']

# Ví dụ sử dụng
image_path = 'path/to/your/image.png'
text = extract_text_from_image(image_path)
translated_text = translate_text(text)
print(translated_text)
