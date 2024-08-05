from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl
from document_processor import process_pdf
from database import Document, initialize_database, db
from contextlib import asynccontextmanager


class PDFLink(BaseModel):
    url: HttpUrl


class ProcessedDocument(BaseModel):
    id: int
    title: str


class DocumentContent(BaseModel):
    id: int
    title: str
    content: str


@asynccontextmanager
async def lifespan(app: FastAPI):
    initialize_database()
    yield


app = FastAPI(lifespan=lifespan)


@app.post("/ingest", response_model=ProcessedDocument)
def ingest_pdf(pdf_link: PDFLink):
    try:
        title, markdown_text = process_pdf(pdf_link.url)
        with db.connection_context():
            document = Document.create(
                title=title, content=markdown_text, url=pdf_link.url
            )
        return ProcessedDocument(id=document.id, title=document.title)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/document/{document_id}", response_model=DocumentContent)
def get_document(document_id: int):
    try:
        with db.connection_context():
            document = Document.get_by_id(document_id)
        return DocumentContent(
            id=document.id, title=document.title, content=document.content
        )
    except Document.DoesNotExist:
        raise HTTPException(status_code=404, detail="Document not found")
