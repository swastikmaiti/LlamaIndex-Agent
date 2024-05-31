from llama_index.core import SimpleDirectoryReader,Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from pypdf import PdfReader
import numpy as np
from llama_index.core import Document
from llama_index.core import SummaryIndex,VectorStoreIndex
from llama_index.core import PromptTemplate
from llama_index.core.tools import QueryEngineTool
from llama_index.core.query_engine.router_query_engine import RouterQueryEngine
from llama_index.core.selectors import LLMSingleSelector

Settings.llm = Ollama(model='phi3',request_timeout=3600.0,temperature=1)
Settings.embed_model = OllamaEmbedding(model_name='nomic-embed-text')

def pre_processing(reader):

    documents_1 = ''
    first_section = "abstract"
    ignore_after = "references"
    pg_no = 0
    for page in reader.pages:
        pg_no += 1
        documents_1 += page.extract_text(0)
    cleaned_string = documents_1.replace('\n', ' ')
    cleaned_string = cleaned_string.lower()

    start_index = cleaned_string.find(first_section)
    end_index = cleaned_string.rfind(ignore_after)
    if start_index!=-1 and end_index!=-1:
        cleaned_string = cleaned_string[start_index:end_index]

    sentence_list = cleaned_string.split('. ')
    context_list = []
    group_size = 20
    overlap = 1
    i = 0 
    while True:
        group = sentence_list[i:i+group_size]
        text = '. '.join(group)
        if len(text)>10:
            context_list.append(text)
        i+=group_size-overlap
        if i>=len(sentence_list):
            break
    return context_list


qa_prompt_tmpl_str = ("<|user|>\n"
    "Context information is below.\n"
    "---------------------\n"
    "{context_str}\n"
    "---------------------\n"
    "Given the context information and not prior knowledge, answer the query\n"
    "Query: {query_str}"
    " <|end|>\n"
    "<|assistant|>"
)

refine_prompt_tmpl_str = ("<|user|>\n"
    "The original query is as follows: {query_str}\n"
    "We have provided an existing answer: {existing_answer}\n"
    "We have the opportunity to refine the existing answer (only if needed) with some more context below.\n"
    "---------------------\n"
    "{context_msg}\n"
    "---------------------\n"
    "Given the new context, refine the original answer to better answer the query. If the context isn't useful, return the original answer."
    " <|end|>\n"
    "<|assistant|>"
)

summary_prompt_tmpl_str = ("<|user|>\n"
    "Context information from multiple sources is below.\n"
    "---------------------\n"
    "{context_str}\n"
    "---------------------\n"
    "Given the information from multiple sources and not prior knowledge, answer the query.\n"
    "Query: {query_str}"
    " <|end|>\n"
    "<|assistant|>"
)

def get_agent(uploaded_pdf):
    reader = PdfReader(uploaded_pdf)
    context_list = pre_processing(reader)
    documents = [Document(text=t) for t in context_list]
    documents_for_summarization = [Document(text=t) for t in context_list[:1]]
    summary_index = SummaryIndex(documents_for_summarization)
    vector_index = VectorStoreIndex(documents)
    

    vector_query_engine = vector_index.as_query_engine(streaming=True)
    summary_query_engine = summary_index.as_query_engine(response_mode="tree_summarize",streaming=True)

    qa_prompt_tmpl = PromptTemplate(qa_prompt_tmpl_str)
    vector_query_engine.update_prompts(
        {"response_synthesizer:text_qa_template": qa_prompt_tmpl}
    )

    refine_prompt_tmpl = PromptTemplate(refine_prompt_tmpl_str)
    vector_query_engine.update_prompts(
        {"response_synthesizer:refine_template": refine_prompt_tmpl}
    )

    summary_prompt_tmpl = PromptTemplate(summary_prompt_tmpl_str)
    summary_query_engine.update_prompts(
        {"response_synthesizer:summary_template": summary_prompt_tmpl}
    )

    summary_tool = QueryEngineTool.from_defaults(
    query_engine=summary_query_engine,
    description=('Useful for summarization or general description questions')
    )

    query_tool = QueryEngineTool.from_defaults(
        query_engine=vector_query_engine,
        description=('Useful for specific questions or topic based questions which are not related to summarization or general description')
    )

    agent = RouterQueryEngine(
    selector=LLMSingleSelector.from_defaults(),
    query_engine_tools=[
        summary_tool,query_tool
    ],
    verbose=True
    )

    return agent
