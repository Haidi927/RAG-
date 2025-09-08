# retriever/retrieve_context.py

import os
import json
from typing import List
from sentence_transformers import SentenceTransformer
from langchain.vectorstores import FAISS, Chroma
from langchain.embeddings import HuggingFaceEmbeddings

# 可配置的参数
VECTOR_BACKEND = "faiss"  # "faiss" or "chroma"
TOP_K = 3

# 索引与原文路径
VECTOR_DIR = "C:/PHD/2025/08/llm/retriever/vector_store"
TEXT_DB_PATH = os.path.join(VECTOR_DIR, "texts.jsonl")

# 初始化嵌入模型（推荐使用 GTE-base 或 BGE-m3）
embedding_model = HuggingFaceEmbeddings(model_name="thenlper/gte-base")

# 加载段落原文（用于检索后获取真实内容）
with open(TEXT_DB_PATH, "r", encoding="utf-8") as f:
    raw_texts = [json.loads(line.strip())["text"] for line in f]

# 加载向量数据库
if VECTOR_BACKEND == "faiss":
    vector_db = FAISS.load_local(VECTOR_DIR, embedding_model, allow_dangerous_deserialization=True)
elif VECTOR_BACKEND == "chroma":
    vector_db = Chroma(persist_directory=VECTOR_DIR, embedding_function=embedding_model)
else:
    raise ValueError("Unsupported VECTOR_BACKEND")


def retrieve_context(query: str, top_k: int = TOP_K) -> List[str]:
    """
    给定输入句子，检索 top_k 个相关背景知识段落。
    返回：List[str]，长度为 top_k，每段为原文字符串。
    """
    docs = vector_db.similarity_search(query, k=top_k)
    return [doc.page_content for doc in docs]
