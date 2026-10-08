from app.embeddings import create_single_embedding
from app.vector_store import get_collection


def retrieve_documents(question, top_k=3):

    collection = get_collection()

    question_embedding = create_single_embedding(question)

    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=top_k
    )

    return results