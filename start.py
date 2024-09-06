from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from typing import Tuple
from agents.lookup import lookup
from dotenv import load_dotenv, find_dotenv
from third_party.linkedin_connect import get_profile
import openai
import os
from output_parsers import summary_parser, Summary

load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate(name: str) -> Tuple[Summary, str]:
    print("indie generate")
    linkedin_username = lookup(name)
    print('url printer', linkedin_username)
    linkedin_data = get_profile(linkedin_profile=linkedin_username, stored = False)
    print('data here',linkedin_data)
    template = """
    Given the Linkedin information {information_here} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    3. Come up with a couple of icebreakers to chat with the person.
    4. Find couple of topics of interest of the person.
    \n{format_instructions}
    """
    p_template = PromptTemplate(
        input_variable=["information_here"],
        template=template,
        partial_variables = {"format_instructions":summary_parser.get_format_instructions()})
    model = "gpt-3.5-turbo"
    llm = ChatOpenAI(model_name=model, temperature=0)
    chain = p_template | llm | summary_parser
    res:Summary = chain.invoke(input={"information_here": linkedin_data})

    return res, linkedin_data.get("profile_pic_url")



if __name__ == '__main__':
    print("ICE BREAKER ENTER")
    # generate(name = "Aman Parikh UCSD")

