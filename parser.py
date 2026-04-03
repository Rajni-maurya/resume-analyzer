import PyPDF2
import docx

def extract_text(file):
    text = ""

    # PDF handling
    if file.filename.endswith('.pdf'):
        pdf = PyPDF2.PdfReader(file)
        for page in pdf.pages:
            text += page.extract_text() or ""

    # DOCX handling
    elif file.filename.endswith('.docx'):
        doc = docx.Document(file)
        for para in doc.paragraphs:
            text += para.text

    # TXT fallback
    else:
        try:
            text = file.read().decode("utf-8")
        except:
            text = ""

    return text.lower()