import os
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from dotenv import load_dotenv
load_dotenv('.env')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

embeddings = OpenAIEmbeddings()
docsearch = Chroma(persist_directory="./data", embedding_function=embeddings)
query = "你是一名券商研究员，帮我解读一下这份研报"
docs = docsearch.similarity_search(query, include_metadata=True)
llm = ChatOpenAI(temperature=0.2,model_name="gpt-3.5-turbo-16k-0613")
chain = load_qa_chain(llm, chain_type="map_reduce", verbose=True)
res = chain.run(input_documents=docs, question=query)
print(res)
