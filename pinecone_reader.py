from langchain.document_loaders import UnstructuredPDFLoader,OnlinePDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
import os
from dotenv import load_dotenv
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone

load_dotenv('.env')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
EPINECONE_NVIRONMENT = os.getenv('EPINECONE_NVIRONMENT')
loader = UnstructuredPDFLoader('../Tabnet.pdf')
data = loader.load()
print(f'文档中{len(data[0].page_content)}字')
text_splitter = RecursiveCharacterTextSplitter(chunk_size=200,chunk_overlap=0)
texts = text_splitter.split_documents(data)
print(f'文本{len(texts)}')


embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
pinecone.init(
    api_key=PINECONE_API_KEY,
    environment=EPINECONE_NVIRONMENT
)
docsearch = Pinecone.from_texts(
    [t.page_content for t in texts],
    embeddings,
    index_name='freshbird')

llm = OpenAI(temperature=0,openai_api_key=OPENAI_API_KEY)
# 基于OpenAI大语言模型构建问答链，分为stuff,map_reduce,refine,map_rerank四种
chain = load_qa_chain(llm=llm,chain_type="stuff")
query = "这篇论文的作者是谁"
docs = docsearch.similarity_search(query)
print("---2--")
result = chain({"input_documents": docs, "question": query}, return_only_outputs=True)
print(result)
