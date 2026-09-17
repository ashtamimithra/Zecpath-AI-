from parsers.resume_extractor import extract_resume 
file_path = "Ashtami K V.pdf" 
result = extract_resume(file_path) 
print("Cleaned Resume Text:\n") 
print(result["cleaned_text"])