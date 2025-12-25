from crewai import Agent
from dotenv import load_dotenv
load_dotenv()
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from crewai import LLM
from tools import tool

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

## Call the model 
# llm=ChatGoogleGenerativeAI(
#     model="gemini/gemini-2.5-flash",
#     verbose=True,
#     temperature=0.5
# )
llm = LLM(
    model="gemini/gemini-2.5-flash",
    temperature=0.5
)

## Creating A senior Researcher agent with memory and verbose mode
researcher=Agent(
    role="Senior Researcher",
    goal="Uncover ground breaking technologies in {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity , you 're at the forefront of"
        "innovation , eager to explore and share knowledge that could change"
        "the world."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True

)

## Create a write agent with custom tools responsible in writing news blog 
news_writer=Agent(
    role='Writer',
    goal='Narrate compelling tech stories about {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics , you craft"
        "engaging narratives that captivate and educate , brining new"
        "discoveries to light in an accessible manner."
    ),
    tools=[tool],
    llm=llm,
    alow_delegation=False



)