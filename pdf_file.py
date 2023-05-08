from pathlib import Path


def get_pdf_file():
    pth = Path().cwd()
    pdf_files = list(pth.glob('*.pdf'))
    return pdf_files[0]
