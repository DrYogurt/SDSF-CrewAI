import datetime
from utils.wiki import SDSF_Wiki as Wiki
from utils.db import ChromaDB

def generate_session_id(raw_prompt: str):
    """
    "get jobs with 'Completed' or 'Started' status"

    ->

    "get_jobs_with_Completed_or_Started_status__12_22_22"
    """

    now = datetime.now()
    hours = now.hour
    minutes = now.minute
    seconds = now.second

    short_time_mm_ss = f"{hours:02}_{minutes:02}_{seconds:02}"

    lower_case = raw_prompt.lower()
    no_spaces = lower_case.replace(" ", "_")
    no_quotes = no_spaces.replace("'", "")
    shorter = no_quotes[:30]
    with_uuid = shorter + "__" + short_time_mm_ss
    return with_uuid

def init_db():
    db_name = "chroma_db"
    collection_name = "wiki"
    db = ChromaDB(db_name, collection_name)
    if db.db is None:
        page_dict = Wiki().get_page_dict()
        contents = [page['content'] for page in page_dict]
        tags = [page['tags'] for page in page_dict]
        db.add_md(contents,tags)

    return db