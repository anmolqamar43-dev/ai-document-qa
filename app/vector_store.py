import chromadb


CHROMA_PATH = "./chroma_db"

client = chromadb.PersistentClient(
    path=CHROMA_PATH
)

collection = client.get_or_create_collection(
    name="document_knowledge"
)


def add_documents(chunks, embeddings, metadatas, ids):
    """
    Store document chunks, embeddings, and metadata
    in ChromaDB.
    """

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas,
        ids=ids
    )


def get_collection():
    """
    Return the ChromaDB collection.
    """

    return collection