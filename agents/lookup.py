import os
from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain_core.tools import Tool
from langchain import hub
from tools.tools import get_profile_url
from langchain.agents import (
    create_react_agent,
    AgentExecutor
)


def lookup(name:str):
    llm = ChatOpenAI(temperature = 0, model_name = 'gpt-3.5-turbo')
    template = """Given the name and information of the person :- {full_name}, I want you to fetch the linkedin profile page which belongs to that person.
    Make sure to only provide the linkedin URL in your answer."""
    print("Hi")
    print(template)
    prompt_template = PromptTemplate(
        template = template,
        input_variables = ["full_name"]
    )
    print(prompt_template)
    tools_for_agent = [
        Tool(
            name = "Linkedin Profile Fetcher",
            func=get_profile_url,
            description = "This is helpful when you want to fetch the linkedin URL of the person who name and information is provided.",
        )
    ]
    react_prompt = hub.pull('hwchase17/react')
    print(react_prompt)
    agent  = create_react_agent(llm=llm, tools=tools_for_agent,prompt = react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools = tools_for_agent, verbose = True)
    print("Hi")
    print(prompt_template.format(full_name=name))
    result = agent_executor.invoke(input={"input": prompt_template.format(full_name=name)})


    print(result)
    url = result['output']
    return url


# if __name__ == "__main__":
    # retrieved_url = lookup(name="Aman Parikh UCSD")
    # print("URL", retrieved_url)


