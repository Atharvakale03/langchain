from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

documents = [
    "Virat Kohli is called the Run Machine for his consistent batting.",
    "Sachin Tendulkar is known as the God of Cricket for his legendary records.",
    "MS Dhoni is famous for his cool captaincy and finishing skills.",
    "Rohit Sharma is called the Hitman for his explosive batting and double centuries.",
    "Kapil Dev led India to its first World Cup victory in 1983."
]

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

query = "Tell me about rohit sharma"

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)

index = scores.argmax()
print("Best match:", documents[index])
print("Similarity score:", scores[0][index])
