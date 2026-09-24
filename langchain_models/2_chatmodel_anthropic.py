from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model="claude-opus-4-1-20250805") # For this we have to the this from cluade anthropic by seraching models
result = model.invoke("What is the capital of France?")
print(result.content)