from langchain.document_loaders import TextLoader
from dotenv import load_dotenv

load_dotenv()

loader = TextLoader("facts.txt")
docs = loader.load()

print(docs)
