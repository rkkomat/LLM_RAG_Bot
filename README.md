# Conversational Retrieval Chain with Langchain and Streamlit

This project implements an interactive conversational system that combines language models with document retrieval, specifically optimized for searching within CSV files. Users can input questions, and the system retrieves relevant answers from the provided data while maintaining a conversational context. The retrieval mechanism uses FAISS (Facebook AI Similarity Search) for fast and efficient document search, powered by OpenAI's language models to generate coherent and context-aware responses.

## Features
 
### Conversational Interface
The app allows users to engage in a conversation-style interaction. Each question from the user builds upon previous exchanges, making the interaction more natural and context-aware.

### CSV Document Search
The project is designed to handle large amounts of textual data stored in CSV format. In this specific case, the `Top_Healthiest_Food.csv` file is used as the knowledge base. This file contains information on healthy foods, and the system retrieves answers by finding relevant content within this document.

### Retrieval-Augmented Responses
Instead of generating answers purely from a model, the app augments responses with real information retrieved from the CSV file. This makes it useful for situations where factual accuracy and specific document-based answers are required.

### Memory of Chat History
The system retains the conversation history between the user and the model during a session. It takes this history into account while generating new responses, which helps maintain the flow of conversation and continuity. For example, if a user asks follow-up questions, the model understands the context and provides coherent responses.

### Flexible Interaction
Users can ask various types of questions about the data (e.g., "What are the top healthiest foods?") and receive answers specifically based on the loaded document. This is ideal for exploring structured datasets like CSVs without manually reading through them.

### Seamless Integration with Streamlit
Streamlit provides a simple and interactive web interface where users can input their queries and view responses. The integration with `streamlit-chat` enables a chat-like experience, making it intuitive for users to interact with the system.

---

## Requirements

1. Python 3.8 or higher
2. OpenAI API key

### Python Libraries
- `os`: Used to handle environment variables such as the OpenAI API key.
- `langchain`: Provides tools for building language model-based applications, including document loaders, vector stores, and retrieval mechanisms.
- `faiss-cpu`: An efficient library for similarity search and clustering of dense vectors, used to store and retrieve document embeddings.
- `openai`: A library to interact with OpenAI's API for generating embeddings and language model outputs.
- `streamlit`: A framework for building web apps easily in Python.
- `streamlit-chat`: Adds a chat interface to the Streamlit app, allowing for more intuitive conversations.

You can install the required packages using pip:
```bash
pip install langchain faiss-cpu openai streamlit streamlit-chat
