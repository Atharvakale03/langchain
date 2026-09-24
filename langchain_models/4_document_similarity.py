from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

documents = [
    "Virat Kohli is called the Run Machine for his consistent batting."
"Sachin Tendulkar is known as the God of Cricket for his legendary records."
"MS Dhoni is famous for his cool captaincy and finishing skills."
"Rohit Sharma is called the Hitman for his explosive batting and double centuries."
"Kapil Dev led India to its first World Cup victory in 1983."
]
embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)
query = 'Tell me about virat kohli'

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)  
scores = cosine_similarity([query_embedding], doc_embeddings)

index, score = sorted(list(enumerate(scores)), key=lambda x: x[1])[-1]
print(documents[index])
print("similarity score is:", score)
