from openai import OpenAI
import os

# 设置代理（如果你用 Clash）
os.environ["HTTP_PROXY"] = "http://127.0.0.1:7890"
os.environ["HTTPS_PROXY"] = "http://127.0.0.1:7890"

# 初始化客户端
client = OpenAI(api_key="")

# 测试一个 Chat Completion
resp = client.chat.completions.create(
    model="gpt-4o-mini",   # 选择 OpenAI 支持的模型
    messages=[
        {"role": "user", "content": "你好，我在中国测试 API 能不能通"}
    ]
)

print(resp.choices[0].message)

