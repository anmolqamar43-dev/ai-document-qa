from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse


from pathlib import Path
from pydantic import BaseModel

from app.rag import answer_question
from fastapi import FastAPI, UploadFile, File, HTTPException

from app.document_loader import load_document
from app.chunker import create_chunks
from app.embeddings import create_embeddings
from app.vector_store import add_documents


app = FastAPI(
    title="AI-Powered Document Question Answering System",
    description="A RAG-based document question answering system.",
    version="1.0.0"
)

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

# Upload folder
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


@app.get("/")
def home():
    return FileResponse("static/index.html")


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    # Check file type
    allowed_extensions = [".pdf", ".txt", ".md"]

    file_extension = Path(file.filename).suffix.lower()

    if file_extension not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail="Only PDF, TXT, and MD files are supported."
        )

    # Save uploaded file
    file_path = UPLOAD_DIR / file.filename

    file_content = await file.read()

    with open(file_path, "wb") as output_file:
        output_file.write(file_content)

    # Load document
    document = load_document(file_path)

    # Create chunks
    chunks = create_chunks(
        document["text"],
        chunk_size=100,
        overlap=20
    )

    if not chunks:
        raise HTTPException(
            status_code=400,
            detail="The uploaded document contains no readable text."
        )

    # Create embeddings
    embeddings = create_embeddings(chunks)

    # Create metadata and IDs
    metadatas = []
    ids = []

    for index, chunk in enumerate(chunks):

        metadatas.append({
            "source": document["filename"],
            "chunk": index
        })

        ids.append(
            f"{Path(file.filename).stem}_{index}"
        )

    # Store in ChromaDB
    add_documents(
        chunks=chunks,
        embeddings=embeddings,
        metadatas=metadatas,
        ids=ids
    )

    return {
        "message": "Document uploaded successfully.",
        "filename": document["filename"],
        "chunks_created": len(chunks)
    }

class QuestionRequest(BaseModel):
    question: str


@app.post("/ask")
def ask_question(request: QuestionRequest):

    if not request.question.strip():
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty."
        )

    result = answer_question(request.question)

    return {
        "question": result["question"],
        "answer": result["answer"],
        "sources": result["sources"],
        "distances": result["distances"]
    }