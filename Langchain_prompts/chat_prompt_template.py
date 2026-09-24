from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import SystemMessage, HumanMessage

chat_template = ChatPromptTemplate([
      'System', 'You are a helpful assistant{domain} expert',
      'Human','Explain the in terms, What is the {topic}?'
])

prompt = chat_template.invoke("domain : cricket","topic : worldcup")

print(prompt)
