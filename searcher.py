import os
os.environ["OPENAI_API_KEY"] = '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'
os.environ["SERPAPI_API_KEY"] = 'cc3833fd7b252842c5f3501b32a7d2ee1213a8dfb2621356e99fbbffa052f4f8'
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI
from langchain.agents import AgentType

# 加载 OpenAI 模型
llm = OpenAI(temperature=0,max_tokens=2048) 

 # 加载 serpapi 工具
tools = load_tools(["serpapi"])
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
agent.run("相比起2022年，2023年Google搜索区块链的人数如何？有多少人在搜索？")
