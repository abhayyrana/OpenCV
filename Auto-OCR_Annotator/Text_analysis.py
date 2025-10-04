""" Text Extraction, Analysis and Pattern Recognition """

import cv2
import pytesseract
import re

def extract_text(image):
    # tesseract prefers RGB format
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pytesseract.image_to_data(rgb, output_type=pytesseract.Output.DICT)
    return results

def detect_important_info(text):
    """
    Identify important information in the extracted text:
    - Names (capitalized words)
    - Dates (various formats)
    - Emails
    - Phone numbers
    """
    if not text or len(text.strip()) < 2:
        return None
    
    # date patterns (12/31/2025, 31-12-2025, Dec 31 2025, 31 Dec 2025)
    date_pattern = r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b|\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{1,2},? \d{4}\b'
    if re.search(date_pattern, text, re.IGNORECASE):
        return "DATE"
    
    # email patterns
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.search(email_pattern, text):
        return "EMAIL"
    
    # phone number patterns
    phone_pattern = r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b|\b\(\d{3}\)\s?\d{3}[-.\s]?\d{4}\b'
    if re.search(phone_pattern, text):
        return "PHONE"
    
    # name detection (capitalized words)
    name_pattern = r'\b[A-Z][a-z]+\s+[A-Z][a-z]+\b'
    if re.search(name_pattern, text):
        return "NAME"
    
    return None

def annotate_doc(image, ocr_results):
    annotate = image.copy()
    n_boxes = len(ocr_results['text'])

    # defining color for different field types
    color_map = {
        "NAME": (0, 255, 0),    # Green
        "DATE": (255, 0, 0),    # Blue
        "EMAIL": (255, 0, 255),   # Purple
        "PHONE": (0, 165, 255)  # Orange
    }

    for i in range(n_boxes):
        confidence = int(ocr_results['conf'][i])
        if confidence > 60:
            text = ocr_results['text'][i]
            field_type = detect_important_info(text)

            if field_type:
                (x, y, w, h) = (ocr_results['left'][i],
                                ocr_results['top'][i],
                                ocr_results['width'][i],
                                ocr_results['height'][i])
                color = color_map.get(field_type, (255, 255, 255))

                # draw rectangle around text
                cv2.rectangle(annotate, (x, y), (x+w, y+h), color, 2)

                # add label above the box
                label = f"{field_type}"
                cv2.putText(annotate, label, (x, y-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    return annotate
