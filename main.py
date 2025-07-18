import os
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from dotenv import load_dotenv
import json

# 加载环境变量
load_dotenv()

def test():
    # 配置DeepSeek API
    llm = ChatOpenAI(
        model="deepseek-chat",
        openai_api_key="sk-8ffa585c55874ab7979ba9e887d2fdc3",
        openai_api_base="https://api.deepseek.com/v1",
        temperature=0.1
    )
    
    # 创建系统消息
    system_message = SystemMessage(content="""
    你是一个专业的Python编程助手。请为用户提供准确、简洁的冒泡排序算法实现。
    只返回可执行的Python代码，不要包含额外的解释或markdown格式。
    """)
    
    # 创建用户消息
    user_message = HumanMessage(content=f"""
    要求：
    1. 实现一个名为bubble_sort的函数
    2. 函数接收一个数组作为参数
    3. 返回排序后的数组
    4. 只返回函数代码，不要包含调用示例
    """)
    
    response = llm.invoke([system_message, user_message])
    generated_code = response.content
    return generated_code
        

    

if __name__ == "__main__":
    print(test())
