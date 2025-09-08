# retriever/build_index.py

import os
import json
from langchain.vectorstores import FAISS, Chroma
from langchain.schema import Document
from langchain.embeddings import HuggingFaceEmbeddings
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

# 参数配置
VECTOR_BACKEND = "faiss"  # 或 "chroma"
VECTOR_DIR = "retriever/vector_store"
TEXTS_PATH = os.path.join(VECTOR_DIR, "texts.jsonl")

# 嵌入模型（可替换为你自己的）
embedding_model = HuggingFaceEmbeddings(model_name="thenlper/gte-base")

# 创建向量库目录（如不存在）
os.makedirs(VECTOR_DIR, exist_ok=True)

# 读取教材/知识段落
raw_texts = []
with open(TEXTS_PATH, "r", encoding="utf-8") as f:
    for line in f:
        try:
            data = json.loads(line.strip())
            raw_texts.append(data["text"])
        except:
            continue

# 转换为 langchain 的 Document 对象
documents = [Document(page_content=text) for text in raw_texts]

# 构建向量库
print(f"📚 正在向量化 {len(documents)} 个知识段落...")

if VECTOR_BACKEND == "faiss":
    db = FAISS.from_documents(documents, embedding_model)
    db.save_local(VECTOR_DIR)
elif VECTOR_BACKEND == "chroma":
    db = Chroma.from_documents(documents, embedding_model, persist_directory=VECTOR_DIR)
    db.persist()
else:
    raise ValueError("Unsupported VECTOR_BACKEND")

print(f"✅ 向量索引已构建完毕，存储于：{VECTOR_DIR}")
