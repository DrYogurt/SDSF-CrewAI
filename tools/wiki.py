from langchain.tools import tool  # Importing the tool decorator
from utils.extras import init_db


db = init_db()  # The database instance
@tool
def search_wiki(query: str, k: int = 10):
    """
    Perform a search on the ChromaDB instance.
    
    Args:
        query (str): The query string to search for.
        k (int, optional): The number of results to return. Defaults to 10.

    Returns:
        list[str]: A list of search results.
    """
    return db.search_db(query, k)

@tool
def write_to_wiki(markdown: str, tags: list[str]):
    """
    Add markdown content to the ChromaDB instance.

    Args:
        markdown (str): The markdown content to add.
        tags (list[str]): A list of tags associated with the markdown content.

    Returns:
        None
    """
    db.add_md([markdown], [tags])