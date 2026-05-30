import chromadb
import os

def retrieve_embedding (user_input):
    db_path = os.getcwd() + "/src/db"
    chroma_client = chromadb.PersistentClient(path=db_path)
    db_collection = chroma_client.get_or_create_collection(name="RAG_Data")
    results = db_collection.query(
        query_texts=[user_input],
        n_results=1
    )
    return results["documents"]
