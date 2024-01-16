from crewai import Agent
from crewai import Agent, Task
from textwrap import dedent

from tools.wiki import search_wiki, write_to_wiki
from tools.markdown import add_hyperlink, write_new_article



class BlogAgents:
    def __init__(self, default_llm=None):
        self.llm = default_llm

    def manager(self, llm=None):
        return Agent(
            role='Wiki Article Manager',
            goal=dedent("""Manage the process of creating a wiki article for a fantasy wiki.
                        Ensure that the article is consistent with existing content.
                        Give small, specific tasks to the other agents to complete the article.
                        If you discover inconsistencies or errors, have the other agents fix them.
                        """),
            backstory=dedent("""I am a specialist in fantasy wiki articles. I provide high quality, 
                                thorough, insightful and actionable feedback via detailed list of changes
                                and actionable tasks.
                             """),
            tools=[],  # Define specific tools here
            llm=self.llm if llm is None else llm,
            verbose=True,
            allow_delegation=True

        )
        
    def worldbuilder(self, llm=None):
        return Agent(
            role='Worldbuilding Expert',
            goal=dedent("""Invent and create compelling events, people and places for the fantasy wiki.
                        Ensure all creations are consistent with existing content.
                        Be creative and use your imagination to create interesting content.
                        Return responses in bullet point form.
                        """),
            backstory=dedent("""I am a seasoned worldbuilder. I work with an existing wiki to craft
                             intricate and interesting details to add to the world.
                             """),
            tools=[search_wiki],  # Define specific tools here
            llm=self.llm if llm is None else llm,
            verbose=True,
            allow_delegation=False

        )
        
    def researcher(self, llm=None):
        return Agent(
            role='Fantasy Wiki Researcher',
            goal=dedent("""Answer questions about the fantasy wiki.
                        Find the most relevant material, and draw connections between different pieces of information.
                        Prioritize the specific details that are requested.
                        Make a note of any details that are missing.
                        Return a pair of bulleted lists, one for the requested details, and one for the missing details.
                        """),
            backstory=dedent("""I am a internet researcher. I specialize in searching databases to find relevant information.
                             I know the wiki is incomplete and should give up if information seems to not exist.
                             """),
            tools=[search_wiki],  # Define specific tools here
            llm=self.llm if llm is None else llm,
            verbose=True,
            allow_delegation=False

        )
    
    def author(self, llm=None):
        return Agent(
            role='Fantasy Wiki Author',
            goal=dedent("""Write a fantasy wiki article from a provided outline.
                        Delegate information gathering to the researcher.
                        Delegate information creation to the worldbuilder.
                        Ensure the article is detailed and interesting.
                        Only include specific details if they are obtained from the outline,
                            the researcher, or the worldbuilder.
                        """),
            backstory=dedent("""I
                             """),
            tools=[],
            llm=self.llm if llm is None else llm,
            verbose=True,
            allow_delegation=True
        )

    def outliner(self, llm=None):
        return Agent(
            role='Fantasy Wiki Outline Writer',
            goal=dedent("""Assign work whenever possible.
                        Write an outline for a fantasy wiki article.
                        Use existing information to create a detailed outline with lots of questions.
                        Delegate to the researcher to research information and if desired information cannot be found, delegate worldbuilding to the worldbuilder.
                        """),
            backstory=dedent("""I am a fantasy wiki outline writer.
                             I work with a team to create compelling outlines for wiki articles.
                             """),
            tools=[],  # Define specific tools here
            llm=self.llm if llm is None else llm,
            verbose=True,
            allow_delegation=True
        )

    
"""

class BlogAgents():
    def __init__(default_llm=None):
        self.llm=llm


    def researcher(self,llm=None):
        return Agent(
                role='Fantasy Wiki Researcher',
                goal='Find the most relevant material in the fantasy wiki',
                backstory='I am a fantasy researcher. I research the fantasy wiki for as much relevant information as I can find',
                tools=[
                #RAG
                ],
                llm = self.llm if llm is None else llm
                verbose=True)


    def writer(self,llm=None):
        return Agent(
                role='Fantasy Wiki Writer',
                goal='Write creative articles with detail. Stay consistent with given information. Invent specific details to create a compelling fantasy world',
                backstory='I am a fantasy writer working on the worldbuilding for my fantasy world. I write creatively, inventing lots of details where needed',
                tools=[
                #Template?
                ],
                llm = self.llm if llm is None else llm
                verbose=True)


    def hyperlinker(self,llm=None):
        return Agent(
                role='Content Hyperlinker',
                goal='Identify specific events, names and locations',
                backstory=,
                tools=[
                # hyperlink adder
                ],
                llm = self.llm if llm is None else llm
                verbose=True)



"""