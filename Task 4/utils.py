import pypdf
import io

def extract_text_from_pdf(pdf_file):
    """
    Extracts text from an uploaded PDF file.

    Args:
        pdf_file: An uploaded file object from Streamlit.

    Returns:
        A string containing the extracted text from the PDF.
    """
    try:
        pdf_reader = pypdf.PdfReader(io.BytesIO(pdf_file.read()))
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        return f"Error extracting text from PDF: {e}"
