
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
import pandas as pd
from langchain.llms.openai import OpenAI

def query_agent(data, query):
    #df = pd.read_csv(data)
    llm =OpenAI()
    agent = create_pandas_dataframe_agent(llm, data, verbose=True)
    return agent.run(query)