import psycopg2

class SDSF_Wiki:
    
    def __init__(self):
        conn = psycopg2.connect(
            host='13.59.0.110',
            port='5432',
            dbname='postgres',
            user='postgres',
            password='penispenispenis'
            )
        self.cur = conn.cursor()
        
    def get_page_dict(self,save=False):
        # Execute a query to get all pages
        self.cur.execute("SELECT id, title, path, content FROM \"pages\"")
        pages = self.cur.fetchall()

        # List to store the pages
        page_dicts = []

        # Iterate over pages and fetch their associated tags and links
        for page in pages:
            page_id, title, path, content = page

            # Fetch tags
            self.cur.execute(f"""
                SELECT t.\"tag\" 
                FROM \"pageTags\" pt 
                JOIN \"tags\" t ON pt.\"tagId\" = t.id
                WHERE pt.\"pageId\" = {page_id}
            """)
            tags = [tag[0] for tag in self.cur.fetchall()]  # Get tag names

            # Fetch links
            self.cur.execute(f"SELECT path FROM \"pageLinks\" WHERE \"pageId\" = {page_id}")
            links = [link[0] for link in self.cur.fetchall()]  # Get link paths

            # Create a dictionary for the page and append it to the list
            page_dict = {
                "name": title,
                "id": page_id,
                "path": path,
                "tags": tags,
                "links": links,
                "content": content
                
            }
            page_dicts.append(page_dict)
            
            # write each dict to a file
            if save:
                with open(f"wiki_pages/{title}.md", "w") as f:
                    f.write(content)
            
        return page_dicts