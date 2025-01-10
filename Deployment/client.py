import requests
import streamlit as st

def get_googleai_response(input_text):
    response=requests.post("http://127.0.0.1:8000/google/invoke",
    json={'input':{'question':input_text}})

    return response.json()['output']

def get_ollama_response(input_text):
    response=requests.post("http://127.0.0.1:8000/ollama/invoke",
    json={'input':{'question':input_text}})

    return response.json()['output']

#streamlit framwork
st.set_page_config(
    page_title="GenBot v1.0",
    page_icon="fav_icon.png",  
)
st.title('GenBot ~ Hub of GenAI Models')

st.sidebar.title("Model Selector")
model_choice = st.sidebar.selectbox("Choose Your Model", ("Gemini 2.0 Flash Exp","Llama 3.2 ~1B"))

user_input = st.text_input("Ask your questions")

if user_input:
    if model_choice == "Gemini 2.0 Flash Exp":
        response = get_googleai_response(user_input)
    elif model_choice == "Llama 3.2 ~1B":
        response = get_ollama_response(user_input)
    else:
        response = "Please select your model in the side bar."

    st.write(f"Reponse from '{model_choice}':")
    st.success(response)    

  
    
