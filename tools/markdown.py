
from langchain.tools import tool  # Importing the tool decorator
from typing import Optional


from langchain.tools import tool  # Importing the tool decorator
from typing import Optional

@tool
def add_hyperlink(article: str, term: str, link: Optional[str] = None) -> str:
    """
    Add a hyperlink to an article.

    Args:
        article (str): The article to add the hyperlink to.
        term (str): The term to hyperlink.
        link (Optional[str]): The link to the term.

    Returns:
        str: The article with the hyperlink.
    """
    print(f"Adding hyperlink to {term}")
    return article.replace(term, f"[{term}]({link})", count=1)


@tool
def write_new_article( title: str, article: str) -> str:
    """
    Writes a new markdown article to a file.

    Args:
        article (str): The text of the article to write.
        title (str): The title of the article.

    Returns:
        str: The article.
    """
    with open(f"wiki/{title}.md", "w") as f:
        f.write(article)
        
    return article
