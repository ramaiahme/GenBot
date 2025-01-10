from fastapi import FastAPI
from langserve import add_routes
from app import chain_google
from app import chain_ollama

app = FastAPI(
    title="GenBot",
    version="1.0",
    description="A Simple API Server"
)

add_routes(app, chain_google, path="/google")
add_routes(app, chain_ollama, path="/ollama")