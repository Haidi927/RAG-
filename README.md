# RAG-
本项目旨在通过 RAG（检索增强生成, Retrieval-Augmented Generation）+ 大语言模型，为食品营养领域构建弱标注数据集。 模块能自动切分文本、检索背景知识，并优化 Prompt，减少人工标注成本，为下游实体关系抽取（NER + RE）任务提供高质量训练样本。
# RAG 驱动的实体关系抽取弱标注模块

## 📌 项目简介
本项目旨在通过 **RAG（检索增强生成, Retrieval-Augmented Generation）+ 大语言模型**，为食品营养领域构建弱标注数据集。  
模块能自动切分文本、检索背景知识，并优化 Prompt，减少人工标注成本，为下游实体关系抽取（NER + RE）任务提供高质量训练样本。  

---

## 🚀 功能特性
- ✅ **轻量化 RAG 模块**：基于 FAISS 构建食品营养知识库，支持向量检索。  
- ✅ **自动弱标注**：输入原始文本，输出 JSON 格式的实体 + 关系标签。  
- ✅ **Prompt 优化**：支持语义增强、约束输出结构。  
- ✅ **低成本高效率**：显著减少人工标注成本，提升模型可用性。  

---

## 🛠 环境配置
```bash
# 创建并激活环境
conda create -n rag_env python=3.10 -y
conda activate rag_env

# 安装依赖
pip install -r requirements.txt
