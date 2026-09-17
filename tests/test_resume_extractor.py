from parsers.resume_extractor import extract_resume,save_cleaned_text 

def test_resume_extraction(): 
    pdf_file_path =r"D:\ZECSER OFFICIAL\Zecpath-AI-\Ashtami K V.pdf" 
    pdf_result = extract_resume(pdf_file_path) 
    assert "cleaned_text" in pdf_result 
    assert len(pdf_result["cleaned_text"]) > 50 
    save_cleaned_text(r"D:\ZECSER OFFICIAL\Zecpath-AI-\resume.txt",pdf_result)

    doc_file_path =r"D:\ZECSER OFFICIAL\Zecpath-AI-\Ashtami K V.docx" 
    doc_result = extract_resume(doc_file_path) 
    # assert "cleaned_text" in doc_result 
    # assert len(doc_result["cleaned_text"]) > 50 
    save_cleaned_text(r"D:\ZECSER OFFICIAL\Zecpath-AI-\document.txt",doc_result)
