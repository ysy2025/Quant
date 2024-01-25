import os
import sys
import time
from pathlib import Path
import pickle
from langchain.document_loaders import DirectoryLoader, Docx2txtLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain.chat_models import ErnieBotChat
from langchain.embeddings import ErnieEmbeddings
from langchain.vectorstores import FAISS
from langchain.schema import format_document

AK = "PykYEOa4Mtc1hSqxQQAZVDKl"
SK = "iDibot290FyTOlFnGkshcreE57gatRRs"

# 本地向量数据库名字
VectorStore_Name = 'vs_faiss'

# 加载文档
def load_documents():
    # 指定要加载的文档所在目录
    docx_path = "document"
    DOCS_ROOT_PATH = "E:\MyGitHub\myPython\MyLLM\document"
    # glob指定加载文件类型 .docx
    # loader_cls指定使用Docx2txtLoader， 就是把docx文件内容转为txt加载
    loader = DirectoryLoader(DOCS_ROOT_PATH, glob="**/*.docx", loader_cls=Docx2txtLoader, loader_kwargs=None)
    # 加载文档
    documents = loader.load()
    return documents

# 分割文档
def split_documents(documents):
    # chunk_size 分割的块大小
    # chunk_overlap 分割的块重复部分大小，0，
    # separators 分隔符列表
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 380,
        chunk_overlap = 0,
        # separators = ["\n\n"],
    )

    documents = text_splitter.split_documents(documents)
    return documents

# 文档向量化和存储
def embed_documents(documents):
    embeddings = ErnieEmbeddings(
        ernie_client_id = AK,
        ernie_client_secret = SK
    )
    if not Path(f'{VectorStore_Name}.pkl').exists():
        # 首次直接从文档创建FAISS
        print("create new vectorstore")
        vectorstore = FAISS.from_documents(documents, embeddings)
    else:
        # 非首次从本地加载FAISS, 再添加文档
        print("load old vectorstore")
        vectorstore = FAISS.load_local(".", embeddings=embeddings, index_name=VectorStore_Name)
        vectorstore.add_documents(documents)
    # 保存到本地
    vectorstore.save_local(".", index_name=VectorStore_Name)

# 提取文档内容向量化
def ingest():
    docs = load_documents()
    print("load documents length: ", len(docs))
    docs = split_documents(docs)
    print("split chunks of document length: ", len(docs))
    embed_documents(docs)
    print("completed!")

# 格式化documents, 只获取page_content
DEFAULT_DOCUMENT_PROMPT = PromptTemplate.from_template(template="{page_content}")
# 合并检索出的文档块
def _combine_documents(docs, document_prompt = DEFAULT_DOCUMENT_PROMPT, document_separator="\n\n"):
    # print(docs)
    doc_strings = [format_document(doc, document_prompt) for doc in docs]
    # print(doc_strings)
    return document_separator.join(doc_strings) if doc_strings else '无相关信息！'

# 通过检索进行问答
def query(question):
    embeddings = ErnieEmbeddings(
        ernie_client_id = AK,
        ernie_client_secret = SK
    )
    vectorstore = FAISS.load_local(".", embeddings=embeddings, index_name=VectorStore_Name)
    # 模板    
    human_template  = """你是一个提供问答助手，请使用以下source标签内的信息来回答问题。如果你不知道答案，就说你不知道，不要试图编造答案。

<source>
{source}
</source>
问题: {question}
回答:
"""
    # 提示
    prompt = ChatPromptTemplate.from_messages([
        ("human", human_template)
    ])
    # chat
    chat_model = ErnieBotChat(
        ernie_client_id = AK,
        ernie_client_secret = SK
    )
    # 创建一个检索器
    retriever = vectorstore.as_retriever()

    # 使用langchain expression language（LCEL）构建一个链(chain)
    full_chain = {
        "source": (lambda x: x["question"]) | retriever | _combine_documents,
        "question": lambda x: x["question"],
    } | prompt | chat_model

    # 调用链
    response = full_chain.invoke({"question": question})
    return response

if  __name__ == "__main__":
    if len(sys.argv) < 2:
        question = input("请输入问题：")
        while question:
            answer = query(question=question)
            print("回答：\n", answer.content)
            question = input("请输入问题：")
    else:
        operation = sys.argv[1]

        if operation == "ingest":
            ingest()
        else:
            print("未知操作:", operation)