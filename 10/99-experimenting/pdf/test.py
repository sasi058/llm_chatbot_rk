from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI(streaming=False)

prompt = ChatPromptTemplate.from_messages([
    ("human", "{content}")
])
messages = prompt.format_messages(content="tell me a joke")

for message in chat.stream(messages):
    print(message.content)
