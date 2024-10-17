import os
from constants import OPENAI_KEY
from langchain.vectorstores import FAISS  
from langchain.embeddings.openai import OpenAIEmbeddings
os.environ["OPENAI_API_KEY"] = OPENAI_KEY
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.chat_models import ChatOpenAI
import streamlit as st
from streamlit_chat import message
loader = CSVLoader(
    file_path='csv_doc\Top_Healthiest_Food.csv',
    )


data = loader.load()

embeddings=OpenAIEmbeddings()

doc_search=FAISS.from_documents(data,embeddings)

chain = ConversationalRetrievalChain.from_llm(
    llm=ChatOpenAI(
        temperature=0.5,
        model_name='gpt-3.5-turbo'
    ),
    retriever=doc_search.as_retriever()
)

def converse_history(query):
    result = chain(
        {"question":query,
         "chat_history":st.session_state['history']})
    st.session_state['history'].append((query,result["answer"]))
    
    return result["answer"]

if 'history' not in st.session_state:
    st.session_state['history']=[]
if 'generated' not in st.session_state:
    st.session_state['generated'] = ["Hello, How can I help you?"]
if 'past' not in st.session_state:
    st.session_state['past']=['Hi']
    
response_container=st.container()
container=st.container()

with container:
    with st.form(key='my_website',clear_on_submit=True):
        customer_input=st.text_input("Query:",placeholder="How can I help you?")
        submite_button=st.form_submit_button(label='Enter')
    if submite_button and customer_input:
        output = converse_history(customer_input)
        
        st.session_state['past'].append(customer_input)
        st.session_state['generated'].append(output)
        
if st.session_state['generated']:
    with response_container:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state['past'][i],is_user=True,key=str(i)+'_user')
            message(st.session_state['generated'][i],key=str(i))
            
