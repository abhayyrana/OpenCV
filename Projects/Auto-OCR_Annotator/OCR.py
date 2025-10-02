"""
Document Scanner & Auto-OCR Annotator
A beginner-friendly OpenCV project for document scanning and text extraction

Author: Abhay Rana
Date: October 2025
"""

import cv2
import numpy as np
import pytesseract
import re
from datetime import datetime
import Doc_detection as dd
import Text_analysis as ta

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Surender Rana\Abhay Rana\SOFTWARES\Tesseract OCR\tesseract.exe'

min_document_area = 1000

def main():
    print("=" * 60)
    print("Document Scanner & Auto-OCR Annotator")
    print("=" * 60)
    print("\nInstructions:")
    print("1. Place a document in front of your webcam")
    print("2. Press 's' to scan and process the document")
    print("3. Press 'q' to quit the application")
    print("4. Press 'r' to reset and scan another document")
    print("\nStarting webcam...")

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return
    
    scanned_doc = None
    annotated_doc = None

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to grab frame.")
            break

        display_frame = frame.copy()
        edged = dd.preprocess_image(frame)
        doc_contour = dd.find_doc_contour(edged)

        if doc_contour is not None:
            cv2.drawContours(display_frame, [doc_contour], -1, (0, 255, 0), 2)
            cv2.putText(display_frame, "Document Detected - Press 's' to Scan", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        else:
            cv2.putText(display_frame, "No Document Detected", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        
        cv2.imshow("Live feed", display_frame)

        if scanned_doc is not None:
            cv2.imshow("Scanned Document", scanned_doc)
        
        if annotated_doc is not None:
            cv2.imshow("Annotated Document", annotated_doc)

        key = cv2.waitKey(1) & 0xFF

        # press 'q' to quit
        if key == ord('q'):
            print("\nExiting application...")
            break

        # press 's' to scan document
        elif key == ord('s') and doc_contour is not None:
            print("\n" + "+"*60)
            print("Scanning document...")

            scanned_doc = dd.tilt_transfrom(frame, doc_contour)
            print("✓ Document straightened.")

            print("\n✓ Performing OCR (this may take a few seconds)...")
            ocr_results = ta.extract_text(scanned_doc)

            annotated_doc = ta.annotate_doc(scanned_doc, ocr_results)
            print("✓ Text extracted and annotated.")

            full_text = " ".join([text for text in ocr_results['text'] if text.strip()])
            print("\n" + "-" * 60)
            print("EXTRACTED TEXT:")
            print("-" * 60)
            print(full_text)
            print("-" * 60)

            print("\nScan complete! Check the \"Annotated Document\" window.")
            print("Press 'r' to reset and scan another document, or 'q' to quit.")
        
        elif key == ord('r'):
            scanned_doc = None
            annotated_doc = None
            cv2.destroyWindow("Scanned Document")
            cv2.destroyWindow("Annotated Document")
            print("\nReset complete! Ready to scan another document.")
        
    cap.release()
    cv2.destroyAllWindows()
    print("Application closed. Goodbye!")

if __name__ == "__main__":
    main()
