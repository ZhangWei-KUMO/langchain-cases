from langchain import OpenAI,PromptTemplate,LLMChain
from langchain.text_splitter import CharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain.docstore.document import Document
from langchain.chains.mapreduce import MapReduceChain
from langchain.chains.summarize import load_summarize_chain
import textwrap
import os
from dotenv import load_dotenv
load_dotenv('.env')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
llm = OpenAI(temperature=0,openai_api_key=OPENAI_API_KEY)
with open('../elon_mask.epub') as f:
    text = f.read()
texts = text_splitter.split_text(text)
# 读取全部文本
docs = [Document(page_content=t) for t in texts[:len(texts)]]
chain = load_summarize_chain(llm, chain_type="map_reduce",verbose=False)
output = chain.run(docs)
wrapped_text = textwrap.fill(output, width=80)
print(output)