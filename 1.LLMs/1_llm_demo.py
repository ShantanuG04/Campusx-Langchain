from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini" , temperature=1.5)

result = llm.invoke("Write a 5 line poem on cricket. ")

print(result.content)