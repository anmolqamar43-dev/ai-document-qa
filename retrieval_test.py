from app.retriever import retrieve_documents


question = "What is semantic search?"


results = retrieve_documents(
    question,
    top_k=3
)


print("\nQUESTION:")
print(question)

print("\nTOP 3 RETRIEVED CHUNKS")
print("=" * 80)


documents = results["documents"][0]
metadatas = results["metadatas"][0]
distances = results["distances"][0]


for index, (document, metadata, distance) in enumerate(
    zip(documents, metadatas, distances),
    start=1
):

    print(f"\nResult {index}")
    print("-" * 80)

    print("Source:", metadata["source"])

    print("Chunk:", metadata["chunk"])

    print("Distance:", distance)

    print("\nText:")
    print(document)