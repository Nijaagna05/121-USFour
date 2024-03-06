import cv2
import pytesseract
import numpy as np

def extract_text_from_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    extracted_text = pytesseract.image_to_string(thresh)
    return extracted_text

def process_extracted_text(text):
    info_dict = {}
    return info_dict

def extract_bill_info(image_path):
    extracted_text = extract_text_from_image(image_path)
    # bill_info = process_extracted_text(extracted_text)
    # return bill_info
    return extracted_text

if __name__ == "__main__":
    image_path = "../test2.jpeg"
    bill_info = extract_bill_info(image_path)
    print(bill_info)