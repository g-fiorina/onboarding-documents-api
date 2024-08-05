# Document Ingestion API

This project implements a document ingestion API using FastAPI. It is designed to receive a PDF link, convert the PDF to Markdown using llmsherpa, and store the PDF title and Markdown content in a PostgreSQL database. The project is organized into several modules and uses environment variables for configuration.

## Project Structure

.
├── src
│   ├── api.py
│   ├── database.py
│   ├── document_processor.py
│   ├── main.py
├── .env
├── .env.example
├── .gitignore
├── requirements.txt

- **`api.py`**: Contains the FastAPI application, including the endpoints for ingesting PDFs and retrieving document content by ID.
- **`database.py`**: Defines the database models and initializes the database connection.
- **`document_processor.py`**: Handles the processing of PDFs, including downloading, converting to Markdown, and extracting titles.
- **`main.py`**: Entry point for running the FastAPI application.
- **`.env`**: Contains environment variables for configuring the application.
- **`.gitignore`**: Specifies files and directories that should be ignored by Git.
- **`requirements.txt`**: Lists the dependencies required for the project.

## Prerequisites

- Python 3.8+
- PostgreSQL
- `pipenv` or `venv` for virtual environment management

## Installation

1. Clone the repository:

  git clone https://github.com/g-fiorina/onboarding-documents-api.git

2. Set up the virtual environment:

  Using venv:
    python -m venv ingest-document-api-env
    source ingest-document-api-env/bin/activate  # On Windows use `ingest-document-api-env\Scripts\activate`

  Using pipenv:
    pip install pipenv
    pipenv shell

3. Install the dependencies:

  pip install -r requirements.txt

4. Configure environment variables:

  Copy the .env.example file to create a new .env file:
    cp .env.example .env

  Open the .env file and update the placeholder values with your actual configuration:
    DATABASE_NAME=ingest-documents-db
    DATABASE_USER=yourusername
    DATABASE_PASSWORD=yourpassword
    DATABASE_HOST=localhost
    DATABASE_PORT=5432
    LLMSHERPA_API_URL=https://genaipoc-pdf-nlm-ingestor.comm-apps.cityinnovate.net/api/parseDocument?renderFormat=all&useNewIndentParser=true

## Running the Application

The database will be initialized automatically when the FastAPI application starts.

Run the FastAPI application :
  fastapi run src/main.py

Access the API documentation:
  Open your web browser and go to http://localhost:8000/docs to view the interactive API documentation provided by Swagger UI.

## API Endpoints

### Ingest PDF

URL: /ingest

Method: POST

Request Body:
{
  "url": "https://example.com/sample.pdf"
}

Response:
{
  "id": 1,
  "title": "Sample Title"
}

### Get Document Content

URL: /document/{document_id}

Method: GET

Response:
{
  "id": 1,
  "title": "Sample Title",
  "content": "Markdown content of the PDF"
}

## Environment Variables

DATABASE_NAME: The name of the PostgreSQL database.
DATABASE_USER: The PostgreSQL user.
DATABASE_PASSWORD: The password for the PostgreSQL user.
DATABASE_HOST: The host of the PostgreSQL database.
DATABASE_PORT: The port of the PostgreSQL database.
LLMSHERPA_API_URL: The API URL for llmsherpa.
