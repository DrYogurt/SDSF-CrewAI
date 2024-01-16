import os
from dotenv import load_dotenv
load_dotenv()


from agents import BlogAgents
from tasks import Tasks

from langchain.chat_models import ChatOpenAI
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chat_models import ChatOllama
from langchain_community.chat_models import ChatLiteLLM

from crewai import Task, Crew, Process
from textwrap import dedent

# Mistral 8000
# OpenHermes 10387
# WizardLM-uncensored 3309

chat_model = lambda model: ChatOllama(
    model=model,
    ollama_address="<IP_ADDRESS_OF_OLLAMA_SERVER>:11434",
    callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
)

mistral = chat_model("mistral")
openhermes = chat_model("openhermes")
wizardlm_uncensored = chat_model("wizardlm-uncensored")


def main():
    # Initialize the agents
    agents = BlogAgents(default_llm=openhermes)
    #manager = agents.manager()
    researcher = agents.researcher(llm=mistral)
    worldbuilder = agents.worldbuilder(llm=wizardlm_uncensored)
    outliner = agents.outliner()
    author = agents.author(llm=wizardlm_uncensored)
    #hyperlinker = agents.hyperlinker()
    user_input = "write an article about the last ruler of Caelun, from the House of Barathon. The article should include three specific events which illustrate the ruler's brutality. You will need to invent these events. Make the name of the article the ruler's name."

    outline_article = Task(
        description=dedent(f"""Work with the researcher and worldbuilder to make an article for the following input:
                           \n{user_input}\n
                           First, work with the researcher to learn some basics of the world.
                           Then, write a detailed outline of the article, including specific questions and details.
                           Next, have the researcher research more detailed information related to the article.
                           Finally, have the worldbuilder create new information related to the article.
                           DO NOT return until the outline is complete.
                           Return the outline of the article as your final output.
                           """),
        agent=outliner
    )
    
    write_article = Task(
        description=dedent(f"""Write a fantasy wiki article from a provided outline.
                           For each section of the outline, use the provided description
                               and questions as guidance on what to write.
                           Ask the researcher for details needed to complete the article.
                           If the researcher cannot find the details, ask the worldbuilder to create them.
                           Return the completed article in markdown format as your final output.
                           """),
        agent=author
    )
    
    
    
    # Create and run the crew
    crew = Crew(
        agents=[outliner, researcher, worldbuilder, author],
        tasks=[outline_article, write_article],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()
    return result


    """
    # User input
    user_input = input("What article would you like us to write? ")
    # Create tasks
    task_manager = Tasks()
    condense_input_task = task_manager.condense_user_input(manager, user_input)
    research_task = task_manager.conduct_research(researcher)
    check_conflict_task = task_manager.check_conflicts(manager)
    write_article_task = task_manager.write_article(author, template=
                                                    #{title}\n\n
                                                    ## Life\n\n{content}
                                                    ### Childhood\n\n{content}
                                                    ### Early Career\n\n{content}
                                                    ### Later Career\n\n{content}
                                                    ### Death and Legacy\n\n{content}
                                                    ## Accomplishments
                                                    ### {accomplishment}\n\n{content}
                                                    ### {accomplishment}\n\n{content}
                                                    ### {accomplishment}\n\n{content}
                                                    
    add_hyperlinks_task = task_manager.add_hyperlinks(hyperlinker)
"""

    

if __name__ == "__main__":
    article = main()
    #print(article)
