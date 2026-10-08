from pathlib import Path
from pypdf import PdfReader


def load_pdf(file_path):
    """Extract text from a PDF file."""

    reader = PdfReader(file_path)

    text = ""

    for page_number, page in enumerate(reader.pages, start=1):
        page_text = page.extract_text()

        if page_text:
            text += f"\n[Page {page_number}]\n"
            text += page_text

    return text


def load_text_file(file_path):
    """Load TXT or Markdown files."""

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def load_document(file_path):
    """
    Load a PDF, TXT, or Markdown document.
    """

    path = Path(file_path)

    extension = path.suffix.lower()

    if extension == ".pdf":
        text = load_pdf(file_path)

    elif extension in [".txt", ".md"]:
        text = load_text_file(file_path)

    else:
        raise ValueError(
            f"Unsupported file type: {extension}"
        )

    return {
        "filename": path.name,
        "text": text
    }