from pathlib import Path

from app.document_loader import load_document
from app.chunker import create_chunks
from app.embeddings import create_embeddings
from app.vector_store import add_documents


DATA_DIR = Path("data")


def ingest_documents():

    all_chunks = []
    all_embeddings = []
    all_metadata = []
    all_ids = []

    document_files = list(DATA_DIR.glob("*"))

    for file_path in document_files:

        if file_path.suffix.lower() not in [".pdf", ".txt", ".md"]:
            continue

        print(f"\nLoading: {file_path.name}")

        document = load_document(file_path)

        chunks = create_chunks(
            document["text"],
            chunk_size=100,
            overlap=20
        )

        print(f"Created {len(chunks)} chunks")

        embeddings = create_embeddings(chunks)

        for index, (chunk, embedding) in enumerate(
            zip(chunks, embeddings)
        ):

            chunk_id = f"{file_path.stem}_{index}"

            all_chunks.append(chunk)

            all_embeddings.append(embedding)

            all_metadata.append({
                "source": document["filename"],
                "chunk": index
            })

            all_ids.append(chunk_id)

    if all_chunks:

        add_documents(
            chunks=all_chunks,
            embeddings=all_embeddings,
            metadatas=all_metadata,
            ids=all_ids
        )

        print("\nDocuments successfully stored in ChromaDB.")

        print(f"Total chunks stored: {len(all_chunks)}")


if __name__ == "__main__":
    ingest_documents()