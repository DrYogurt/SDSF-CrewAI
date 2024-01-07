from crewai import Agent


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



