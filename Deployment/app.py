import os 
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
#loaing GoogleAPI
os.environ['GOOGLE_API_KEY']=os.getenv("google_apikey")

## Langsmith Tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("langchain_apikey")

#llm Google model=Gemini-2.0-flash-exp
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp")

#llm Ollama model=llama3.2:1b
llm_ollama = OllamaLLM(model="llama3.2:1b")

#prompt template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please reposne to the user queries"),
        ("user","Question:{question}")
    ]
)

#chain
output_parser=StrOutputParser()
chain_google=prompt|llm|output_parser
chain_ollama=prompt|llm_ollama|output_parser