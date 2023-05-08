import PyPDF2


def pdf_to_audio(filepath):
    pdf_reader = PyPDF2.PdfReader(filepath)
    for page in range(len(pdf_reader.pages)):
        text = pdf_reader.pages[page].extract_text()
        clean_text = text.strip().replace('\n', ' ')
    return clean_text
