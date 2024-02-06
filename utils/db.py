from langchain_community.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
import os, chromadb

class ChromaDB:
    def __init__(self, db_name, collection_name):
        self.collection_name = collection_name
        self.db = None
        self.db_name = db_name
        if self.db_name in os.listdir():
            try:
                self.db = Chroma(persist_directory=f"./{self.db_name}",embedding_function=OpenAIEmbeddings())
            except Exception as e:
                print(f"Could not load database. New database will be created when first adding files.\n{e}")
        #self.collection = self.persistent_client.get_or_create_collection(collection_name, embedding_function=emb_fn)
        #self.db = Chroma(
        #    client=self.persistent_client,
        #    collection_name=collection_name,
        #    embedding_function=emb_fn
        #)
        self.max_id = 0

    def add_or_init_db(self, splits):
        if len(splits) == 0:
            return
        ids = [str(i+self.max_id) for i in range(1, len(splits) + 1)]
        self.max_id += len(splits)
        if self.db is None:
            self.db = Chroma.from_documents(splits,
                                            ids=ids,
                                            embedding=OpenAIEmbeddings(),
                                            persist_directory=f"./{self.db_name}",
            )
        else:
            self.db.add_documents(
                splits,
                ids=ids,
                )
                
    
    def add_md(self, markdowns, tags=None, chunk_size=250, chunk_overlap=30):
        markdown_splitter = MarkdownHeaderTextSplitter(
            headers_to_split_on=[
                ("#", "Header 1"),
                ("##", "Header 2"),
                ("###", "Header 3"),
                ("####", "Header 4"),
            ],
            strip_headers=True
        )
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size, chunk_overlap=chunk_overlap
        )
        
        for md, tag in zip(markdowns, tags):
            md_header_splits = markdown_splitter.split_text(md)
            splits = text_splitter.split_documents(md_header_splits)
            self.add_or_init_db(splits)

    
    
    def search_db(self, query: str, k=10) -> list[str]:
        """searches the database for information similar to the query

        Args:
            query (str): the query to search for
            k (int, optional): the number of results to return. Defaults to 10.

        Returns:
            list[str]: the results of the search, ranked by similarity
        """
        results = self.db.similarity_search(query, k=k)
        return [doc.page_content for doc in results]