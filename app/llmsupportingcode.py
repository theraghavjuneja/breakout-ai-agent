from langchain_community.utilities import SerpAPIWrapper
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.agents import (
    Tool,
    AgentExecutor,
    create_react_agent)
 
search=SerpAPIWrapper()
tools = [Tool(name="Get Answers", func=search.run, description="This tool will help you search for any information of google if you give a good and specific search term")]

load_dotenv()
params = {
    "engine": "google",
    "gl": "in",
    "google_domain":"google.co.in",
    "hl": "en",
}
llm=ChatGroq(model_name="llama-3.1-70b-versatile",temperature=0.2)
template = '''Answer the following questions as best you can. You have access to the following tools:
{tools}
Use the following format:
Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question
If there is one answer just return it
If there are more than one answers return all of them separated by commas
Begin!
Question: {input}
Thought:{agent_scratchpad}'''
prompt = PromptTemplate.from_template(template)
search_agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(
    agent=search_agent,
    tools=tools,
    verbose=True,
    
)
# Now i should map all of the requests to a single