import chromadb
import json


def read_json_from_file(filename):
    with open(filename, "r", encoding="utf8") as f:
        data = f.read()
        return json.loads(data)


genesis_documents = []
genesis_metadata = []
genesis_ids = []

genesis = read_json_from_file("genesis.json")

# For each chapter in the json data:
for chapter in genesis["chapters"]:
    # For each verse in the chapter:
    for verse in chapter["verses"]:
        # Create a document with the verse text
        genesis_documents.append(verse["text"])
        # Create a metadata object with the chapter and verse number
        genesis_metadata.append(
            {"chapter": chapter["chapter"], "verse": verse["verse"]}
        )
        # Create an id for the document
        genesis_ids.append(f"{chapter['chapter']}:{verse['verse']}")

chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="genesis")
collection.add(documents=genesis_documents, metadatas=genesis_metadata, ids=genesis_ids)

print("Size of Collection:", collection.count())

queries = [
    "God",
    "God Creates",
    "Children made in the image of God",
    "God is love",
    "God is angry",
    "How long do people live?",
]

for query in queries:
    print(f"Query: {query}")
    results = collection.query(query_texts=[query], n_results=5)
    # Results contains documents, metadatas, and distances
    for doc, metadata, distance in zip(
        results["documents"][0], results["metadatas"][0], results["distances"][0]
    ):
        print(
            f"- Chapter {metadata['chapter']}, Verse {metadata['verse']} ({distance:.2f}): {doc}"
        )
        print()
    print()
