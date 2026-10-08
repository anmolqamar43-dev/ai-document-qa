from app.rag import answer_question


questions = [
    "What is Artificial Intelligence?",
    "What is Machine Learning?",
    "What are text embeddings?",
    "How does semantic search work?",
    "What is Retrieval-Augmented Generation?"
]


for question in questions:

    print("\n" + "=" * 80)

    print("QUESTION:")
    print(question)

    print("=" * 80)

    result = answer_question(question)

    print("\nANSWER:")
    print(result["answer"])

    print("\nSOURCES:")

    for source in result["sources"]:
        print(
            f"- {source['source']} "
            f"(chunk {source['chunk']})"
        )

    print("\nDISTANCES:")

    for distance in result["distances"]:
        print(f"- {distance}")