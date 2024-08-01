from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl
from document_processor import process_pdf
from database import Document, initialize_database
from contextlib import contextmanager

app = FastAPI()


class PDFLink(BaseModel):
    url: HttpUrl


class ProcessedDocument(BaseModel):
    title: str
    markdown: str


@contextmanager
def startup_event():
    initialize_database()
    yield


@app.post("/ingest", response_model=ProcessedDocument)
def ingest_pdf(pdf_link: PDFLink):
    try:
        title, markdown_text = process_pdf(pdf_link.url)
        document = Document.create(title=title, content=markdown_text)
        return ProcessedDocument(title=document.title, markdown=document.content)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
