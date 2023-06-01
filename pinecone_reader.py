from langchain.document_loaders import UnstructuredPDFLoader,OnlinePDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain

loader = UnstructuredPDFLoader('../book.pdf')
data = loader.load()
print(f'文档中{len(data[0].page_content)}字')
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=0)
texts = text_splitter.split_documents(data)
print(f'文本{len(texts)}')
from langchain.vectorstores import Chroma,Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone

embeddings = OpenAIEmbeddings(openai_api_key='')
pinecone.init(
    api_key='',
    environment=''
)
index_name="langchain_test"
docsearch = Pinecone.from_texts([t.page_content for t in texts],embeddings,index_name=index_name)

# query = "TabNet算法是什么？"
llm = OpenAI(temperature=0,openai_api_key='')
chain = load_qa_chain(llm=llm,chain_type="stuff")
query = "这本书的内容是啥？"
docs = docsearch.similar_documents(query, include_metadata=True)
chain.run(input_document=docs, question=query)
