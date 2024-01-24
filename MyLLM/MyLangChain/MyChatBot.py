"""
https://zhuanlan.zhihu.com/p/672816626
https://blog.csdn.net/qq_45156060/article/details/134072123
"""

import tkinter as tk
from tkinter import scrolledtext, messagebox
import SparkApi

# 以下密钥信息从控制台获取
# appid = ""  # 填写控制台中获取的 APPID 信息
# api_secret = ""  # 填写控制台中获取的 APISecret 信息
# api_key = ""  # 填写控制台中获取的 APIKey 信息

# 用于配置大模型版本，默认“general/generalv2”
domain = "generalv3"  # v3.0版本
temperature = 0.5
top_k = 4
max_tokens = 2048  # 最大生成长度为8192

# 云端环境的服务地址
Spark_url = "wss://spark-api.xf-yun.com/v3.1/chat"  # v3.0环境的地址

text = []


def getText(role, content):
    jsoncon = {"role": role, "content": content}
    text.append(jsoncon)
    return text


def getlength(text):
    return sum(len(content["content"]) for content in text)


def checklen(text):
    while getlength(text) > 8000:
        del text[0]
    return text


class SparkChatbotGUI:
    def __init__(self, master):
        self.master = master
        master.title("星火API")

        # 创建主框架，用于容纳文本区域和参数设置
        self.main_frame = tk.Frame(master)
        self.main_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # 创建文本显示区域
        self.text_area = scrolledtext.ScrolledText(self.main_frame, wrap=tk.WORD, font=("TkDefaultFont", 14))
        self.text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # 创建参数设置区域框架
        self.parameters_frame = tk.Frame(self.main_frame)
        self.parameters_frame.pack(side=tk.RIGHT, fill=tk.Y, expand=False)

        # 参数设置区域内的具体参数
        self.domain_label = tk.Label(self.parameters_frame, text="模型:1、2、3")
        self.domain_label.pack(side=tk.TOP, fill="x", expand=False)
        self.domain_entry = tk.Entry(self.parameters_frame)
        self.domain_entry.pack(side=tk.TOP, fill="x", expand=False)
        self.domain_entry.insert(0, domain)

        self.temperature_label = tk.Label(self.parameters_frame, text="随机性:0-1")
        self.temperature_label.pack(side=tk.TOP, fill="x", expand=False)
        self.temperature_entry = tk.Entry(self.parameters_frame)
        self.temperature_entry.pack(side=tk.TOP, fill="x", expand=False)
        self.temperature_entry.insert(0, str(temperature))

        self.top_k_label = tk.Label(self.parameters_frame, text="多样性:1-6")
        self.top_k_label.pack(side=tk.TOP, fill="x", expand=False)
        self.top_k_entry = tk.Entry(self.parameters_frame)
        self.top_k_entry.pack(side=tk.TOP, fill="x", expand=False)
        self.top_k_entry.insert(0, str(top_k))

        self.max_tokens_label = tk.Label(self.parameters_frame, text="最大Tokens:V3-8192")
        self.max_tokens_label.pack(side=tk.TOP, fill="x", expand=False)
        self.max_tokens_entry = tk.Entry(self.parameters_frame)
        self.max_tokens_entry.pack(side=tk.TOP, fill="x", expand=False)
        self.max_tokens_entry.insert(0, str(max_tokens))

        # 在参数设置区域内添加复制按钮
        self.copy_button = tk.Button(self.parameters_frame, text="复制", command=self.copy_output)
        self.copy_button.pack(side=tk.BOTTOM, fill="x", expand=False, pady=5)

        # 创建输入框和按钮的框架
        self.entry_frame = tk.Frame(master)
        self.entry_frame.pack(fill=tk.X, padx=10, pady=5)

        # 创建输入框
        self.entry = tk.Entry(self.entry_frame, font=("TkDefaultFont", 14))
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 20))
        self.entry.bind("<Return>", self.send_message_event)  # 绑定回车键

        # 创建发送按钮
        self.send_button = tk.Button(self.entry_frame, text="发送", command=self.send_message)
        self.send_button.pack(side=tk.LEFT, padx=(20, 10))

        # 创建清除记录按钮
        self.clear_button = tk.Button(self.entry_frame, text="清除记录", command=self.clear_records)
        self.clear_button.pack(side=tk.LEFT)

    def send_message_event(self, event):
        self.send_message()

    def send_message(self):
        user_input = self.entry.get()
        question = checklen(getText("user", user_input))
        # 更新API调用参数
        domain = self.domain_entry.get()
        temperature = float(self.temperature_entry.get())
        top_k = int(self.top_k_entry.get())
        max_tokens = int(self.max_tokens_entry.get())
        # 调用API
        SparkApi.answer = ""
        SparkApi.main(Spark_url, domain, question)
        # 更新文本区域
        self.update_text_area(SparkApi.answer + "")
        self.entry.delete(0, tk.END)

    def update_text_area(self, message):
        self.text_area.insert(tk.END, message)
        self.text_area.yview(tk.END)

    def copy_output(self):
        self.master.clipboard_clear()
        self.master.clipboard_append(self.text_area.get("1.0", tk.END))

    def clear_records(self):
        # 清除文本区域的内容
        self.text_area.delete('1.0', tk.END)
        # 重置保存的历史记录
        global text
        text = []


if __name__ == '__main__':
    root = tk.Tk()
    app = SparkChatbotGUI(root)

    # 设置窗口初始大小
    window_width = 1000
    window_height = 600
    root.geometry(f"{window_width}x{window_height}")

    # 获取屏幕尺寸以计算布局参数，使窗口居中
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # 计算x, y坐标以使窗口在屏幕上居中
    center_x = int((screen_width / 2) - (window_width / 2))
    center_y = int((screen_height / 2) - (window_height / 2))

    # 设置窗口的初始位置
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    root.mainloop()