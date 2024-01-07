https://www.gettingstarted.ai/tutorial-chroma-db-best-vector-database-for-langchain-store-embeddings/

import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions
from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings

class ChromaDBManager:
   def __init__(self, embedding_model, db_name):
       self.embedding_function = SentenceTransformerEmbeddings(model_name=embedding_model)
       settings = Settings(persist_directory=db_name)
       self.client = chromadb.PersistentClient(settings=settings)
       self.collection = self.client.get_or_create_collection(db_name)

   def add_to_db(self, filenames):
       documents = []
       ids = []
       for filename in filenames:
           with open(filename, 'r') as file:
               content = file.read()
               documents.append(content)
               ids.append(filename)
       embeddings = self.embedding_function(documents)
       self.collection.add(ids=ids, documents=documents, embeddings=embeddings)

   def search_db(self, query):
       return self.collection.query(query_texts=[query], n_results=2)

