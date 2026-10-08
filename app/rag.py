from app.retriever import retrieve_documents
from app.llm import generate_answer


def build_context(results):
    """
    Convert retrieved chunks into a single context string.
    """

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    context_parts = []

    for index, (document, metadata) in enumerate(
        zip(documents, metadatas),
        start=1
    ):
        source = metadata.get("source", "Unknown")

        context_parts.append(
            f"""
Source {index}: {source}

{document}
"""
        )

    return "\n".join(context_parts)


def build_rag_prompt(question, context):
    """
    Create the final prompt using the retrieved context.
    """

    return f"""
You are an AI document question answering assistant.

Answer the user's question using ONLY the information
provided in the context below.

Do not use outside knowledge.

If the answer cannot be found in the provided context,
say:

"I could not find the answer in the provided documents."

Keep the answer clear, accurate, and concise.

---------------- CONTEXT ----------------

{context}

-------------- END CONTEXT --------------

Question:
{question}

Answer:
"""


def answer_question(question):
    """
    Complete RAG pipeline:

    1. Retrieve relevant chunks
    2. Build context
    3. Create prompt
    4. Ask the LLM
    5. Return answer and sources
    """

    # Step 1: Retrieve top 3 chunks
    results = retrieve_documents(
        question,
        top_k=3
    )

    # Step 2: Build context
    context = build_context(results)

    # Step 3: Create RAG prompt
    prompt = build_rag_prompt(
        question,
        context
    )

    # Step 4: Generate answer
    answer = generate_answer(prompt)

    # Step 5: Extract sources
    sources = results["metadatas"][0]

    return {
        "question": question,
        "answer": answer,
        "context": context,
        "sources": sources,
        "distances": results["distances"][0]
    }