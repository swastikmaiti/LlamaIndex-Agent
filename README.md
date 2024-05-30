# AGENTIC-RAG

An Llama Index based Agentic-RAG system to perform PDF Question-Answering. The Agent can choose from `summarization query engine` or `vector query engine` to generate response. 
The LLM used is `phi3` 3.8B.


![alt text](https://github.com/swastikmaiti/AGENTIC-RAG/blob/60c5c4efca56eb535901cbed9b4d2d577712c9b4/agentic_rag-1.png)

# Frameworks
- ***Agentic-RAG:*** Llama Index
- ***App:*** Gradio
- ***LLM:*** Phi3 3.8B
- ***Embedding:*** nomic-embed-text
- ***Local LLM:*** Ollama

# File Structure
- ***llamaindex_basic.ipynb:*** A simple introduction to Llama Index Agentic RAG concepts and terminologies.
- ***agentic_rag_intro.ipynb:*** This notebook contains codes and step by step explanation of how to build an Agentic-RAG with Llama Index.
- ***agentic_rag_customization.ipynb*** Customizing the Agentic-RAG system to perform pdf Q/A with Phi3
- ***utils.py*** Contains all the functions in one place.
- ***app.py*** Creating Gradio application.
  

# Introduction 
RAG is a wonderful solution to make LLM even smarter with Memeory. However RAG is a single end2end pipeline. User will have various kind of queries which will 
require diffrent kind of processing with a specialized pipeline. This is where AGENTIC-RAG comes into action. A smart AGENT takes dicesion based on user queries and avaialble pipelines to 
fireup one or more of the pipelines to answer user queries.

# Docker 
For Docker Implementation of the Application Checkout the [GitHub Repo](https://github.com/swastikmaiti/AGENTIC-RAG-DOCKER.git). 🚛


# Description
In this work we build a Agentic RAG with llamaindex. Retrieval Augmented Generation (RAG) is one of the most widespread usecase of LLM.
In RAG there exist a single pipeline for the workflow. Hence all user queries are processed in exactly the same way. However there exist different types 
of user queries which may require different pipenine for processing. In this work we build two piplines to answer user queries with specific need. The pipelines are
- Summarization pipeline
- Question-Answering pipeline

# Decription of files in sequence they were developed
The code description are provided within the files.
- llamaindex_basic.ipynb: a brief intro on llamaindex framework
- agentic_rag_intro.ipynb: a brief introduction to agentic rag development.
- agentic_rag_customization.ipynb: the notebook for complete code on developing the agentic rag to answer user queries from a pdf file.
- app.py: finally build a Application with Gradio. This is build on top of `agentic_rag_customization.ipynb` so all the necessary functions are present in `utils.py`.

# How to RUN
- All the work is developed in LINUX env so we need a LINUX system with atleast 8GB RAM.
- Create a Virtual Env
- Install libraries with `make install`
- Download Ollama and start Ollama server with `make ollama_download` on a new CLI as this will block the CLI.
- Pull models required for tasks with `make models`
- To Start Graio App run `python app.py`

# Acknowledgements
- Thanks to DeepLearning.AI and LlamaIndex for the wonderful [course](https://www.deeplearning.ai/short-courses/building-agentic-rag-with-llamaindex/?utm_campaign=llamaindexC2-launch&utm_medium=headband&utm_source=dlai-homepage)
- Thanks to `Microsoft` for open source Phi3

