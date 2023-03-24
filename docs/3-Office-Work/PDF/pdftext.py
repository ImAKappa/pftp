"""pdftext

This module extracts text from PDFs
"""
from pathlib import Path
from PyPDF2 import PdfReader
from io import StringIO
from typing import Optional


def describe_pdf(pdf: PdfReader) -> None:
    """Describes properties of the PDF

    :param pdf: PdfReader Object
    """
    print("Metadata".center(20, "="))
    for field, data in pdf.metadata.items():
        field = field.strip("/")
        print(f"{field:<20}{data}")
    print(f"{'Pages':<20}{len(pdf.pages)}")


def extract_all_text(pdf: PdfReader, pages: Optional[range] = None) -> str:
    """Extracts text from every page in the document

    :param pdf: PdfReader object
    :param pages: Selected page numbers. This range is INCLUSIVE
    """
    text = StringIO()
    if not pages:
        pages = range(len(pages))
    else:
        # Convert page numbers to indices
        pages = range(pages.start - 1, pages.stop, pages.step)
    for page_idx in pages:
        page_number = page_idx + 1
        page_divider = f"Page {page_number}".center(20, "=")
        text.write(f"\n{page_divider}\n")
        page = pdf.pages[page_idx]
        text.write(page.extract_text())
    return text.getvalue()


def main():
    # File source: https://www.almanac.com/sites/default/files/webform/pdf/almanac-start-a-garden.pdf
    file = Path("./almanac-start-a-garden.pdf")
    print(f"Extracting text from '{file.absolute()}'")

    with open(file, mode="rb") as f:
        my_pdf = PdfReader(f)
        describe_pdf(my_pdf)
        text = extract_all_text(my_pdf, pages=range(1, 3))
    print(text)


if __name__ == "__main__":
    program_name = "PDF Text Extractor"
    print(f"{program_name}\n{'-'*len(program_name)}")
    main()
