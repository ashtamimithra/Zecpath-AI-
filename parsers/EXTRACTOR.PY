import os
import re
from PyPDF2 import PdfReader
# from docx import Document 

def extract_text_from_pdf(path):
    text = "" 
    reader = PdfReader(path) 
    for page in reader.pages: 
        text += page.extract_text() + "/n"
    return text 

# def extract_text_from_docx(path): 
    doc = Document(path) 
    return "/n".join([para.text for para in doc.paragraphs]) 



def clean_text(text):
    text = re.sub(r"[^a-zA-Z0-9\s\.\,\-\n]", "", text)
    text = re.sub(r"\s+", " ", text)  
    text = text.replace("•", "-").replace("●", "-") 
    text = text.strip() 
    return text
 
def normalize_sections(text): 
    replacements = { "WORK EXPERIENCE": "Experience", "PROFESSIONAL EXPERIENCE": "Experience", "EDUCATION DETAILS": "Education", "SKILLS SET": "Skills" } 
    for key, value in replacements.items(): 
        text = text.replace(key, value)
    return text

def extract_resume(path):
    ext = path.split(".")[-1] 
    if ext == "pdf": 
        raw_text = extract_text_from_pdf(path)
    elif ext == "docx": 
        raw_text = extract_text_from_docx(path)
    else:
        raise ValueError("Unsupported file format")
    cleaned = clean_text(raw_text) 
    normalized = normalize_sections(cleaned)
    return { "file_name": os.path.basename(path), "raw_text": raw_text, "cleaned_text": normalized } 

print(extract_resume(r"D:\ZECSER OFFICIAL\Zecpath-AI-\Ashtami K V.pdf"))