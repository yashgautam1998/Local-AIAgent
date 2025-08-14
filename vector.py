from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

#Deta frame for reading csvfile
#Models for generating vector embeddings

df = pd.read_csv("Restaurants_Reviews.csv")

embeddings = OllamaEmbeddings(model="mxbai-embed-large")

#Location of folder for storing our vector database
db_location = "./chrome_langchain_db"
add_documents = not os.path.exists(db_location)
add_location=not.os

if add_documents:
    documents = []
    ids = []

    for i, row in df.iterrows():
        document = Document(
            page_content=row["Title"] + " " + row["Review"],
            metadata={"rating": row["Rating"], "date": row["Date"]},
            id=str(i)
        )
        ids.append(str(i))
        documents.append(document)

vector_store = Chroma(
    collection_name="restaurant_reviews",
    persist_directory=db_location,
    embedding_function=embeddings
)

if add_documents:
    vector_store.add_documents(documents=documents , ids=ids)

retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}
)