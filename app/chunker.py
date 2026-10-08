def create_chunks(text, chunk_size=100, overlap=20):
    """
    Split text into overlapping chunks.

    chunk_size:
        Number of words in each chunk.

    overlap:
        Number of words shared between consecutive chunks.
    """

    words = text.split()

    chunks = []

    start = 0

    while start < len(words):

        end = start + chunk_size

        chunk = " ".join(words[start:end])

        if chunk.strip():
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks