# AGENTIC-RAG
building a agentic rag with llamaindex to answer user queries with a specialized workflow pipeline.

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
- Download Ollama and Start Server with `make ollama_download`
- Pull models required for tasks with `make models`
- To Start Graio App run `python app.py`

