from llmsherpa import readers
import requests
import fitz  # PyMuPDF
import os
from dotenv import load_dotenv

load_dotenv(override=True)

llmsherpa_api_url = os.getenv("LLMSHERPA_API_URL")


def process_pdf(pdf_url):
    response = requests.get(url=pdf_url, timeout=100)
    response.raise_for_status()

    pdf_reader = readers.file_reader.LayoutPDFReader(llmsherpa_api_url)
    document = pdf_reader.read_pdf(path_or_url="", contents=response.content)

    markdown_text = document.to_text()

    pdf_document = fitz.open(stream=response.content, filetype="pdf")
    title = pdf_document.metadata.get("title", "No Title Found")
    pdf_document.close()

    return title, markdown_text
