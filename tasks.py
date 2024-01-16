from crewai import Task
from textwrap import dedent
from datetime import date

class Tasks:
    def condense_user_input(self, agent, user_input):
        # Task for condensing user input
        return Task(
            description=f"""Read the following user input and condense it into key points: {user_input}""",
            agent=agent
        )

    def conduct_research(self, agent):
        # Task for conducting research based on user input
        return Task(
            description=f"""Conduct research on the following topic and compile relevant information""",
            agent=agent
        )

    def check_conflicts(self, agent):
        # Task for checking if new information conflicts with existing information
        return Task(
            description=f"""Review the following research output and confirm if there are any conflicts with existing information""",
            agent=agent
        )

    def write_article(self, agent, template):
        # Task for writing the article based on bullet points and template
        return Task(
            description=f"""Write an article using the research done and the following template: {template}, and save it using the write_new_article function""",
            agent=agent
        )

    def add_hyperlinks(self, agent):
        # Task for identifying terms and adding hyperlinks in the article
        return Task(
            description=f"""Identify key terms in the following article text and add hyperlinks to relevant articles or create new ones""",
            agent=agent
        )