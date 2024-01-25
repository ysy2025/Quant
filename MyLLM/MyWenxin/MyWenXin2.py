from langchain_community.embeddings import QianfanEmbeddingsEndpoint
from langchain_community.llms.baidu_qianfan_endpoint import QianfanLLMEndpoint
from langchain_wenxin.llms import Wenxin, BaiduCommon
import os

from langchain_community.chat_models import QianfanChatEndpoint
from langchain_core.language_models.chat_models import HumanMessage

if __name__ == '__main__':
    ak = "PykYEOa4Mtc1hSqxQQAZVDKl"
    sk = "iDibot290FyTOlFnGkshcreE57gatRRs"

    chat = QianfanChatEndpoint(streaming=True)
    chat.qianfan_ak = ak
    chat.qianfan_sk = sk
    messages = [HumanMessage(content="Hello")]
    chat.invoke(messages)
    # endpoint = QianfanEmbeddingsEndpoint()
    # llmEndpoint = QianfanLLMEndpoint()
    """
    还是验证失败
    """