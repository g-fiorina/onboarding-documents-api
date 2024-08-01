from llmsherpa import readers
import requests
import fitz  # PyMuPDF
import os
import json

with open("config/config.json") as f:
    config = json.load(f)
    llmsherpa_api_url = config["LLMSHERPA_API_URL"]


def download_pdf(pdf_url):
    response = requests.get(pdf_url)
    response.raise_for_status()

    pdf_path = "temp.pdf"

    with open(pdf_path, "wb") as pdf_file:
        pdf_file.write(response.content)

    return pdf_path


def convert_pdf_to_markdown(pdf_path):
    pdf_reader = readers.file_reader.LayoutPDFReader(llmsherpa_api_url)
    document = pdf_reader.read_pdf(path_or_url=pdf_path)
    markdown_text = document.to_text()

    return markdown_text


def extract_pdf_title(pdf_path):
    pdf_document = fitz.open(pdf_path)
    metadata = pdf_document.metadata
    title = metadata.get("title", "No Title Found")
    pdf_document.close()

    return title


def process_pdf(pdf_url):
    pdf_path = download_pdf(pdf_url)

    try:
        markdown_text = convert_pdf_to_markdown(pdf_path)
        title = extract_pdf_title(pdf_path)

    finally:
        os.remove(pdf_path)

    return title, markdown_text
