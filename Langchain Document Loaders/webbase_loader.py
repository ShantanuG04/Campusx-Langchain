from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template="Answer the following question \n {question} from the following text - \n {text}",
    input_variables=["question","text"]
)

parser = StrOutputParser()

url = "https://www.flipkart.com/item/p/product?pid=MOBHQDMKCCDK2VT7&marketplace=FLIPKART&pageUID=1792682367883"

loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | parser

print(chain.invoke({'question':'What is the RAM of this product?' , 'text':docs[0].page_content}))

# print(len(docs))

# print(docs[0].page_content)
