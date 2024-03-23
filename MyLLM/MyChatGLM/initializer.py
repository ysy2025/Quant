# from transformers import AutoTokenizer，AutoModel
#
# tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm-6b"，trust_remote_code=True)
# model = AutoModel.from_pretrained("THUDH/chatglm-6b"， trust_remote_code=True).half().cuda()
# model = model.eval()
# response，history = model.chat(tokenizer，"你好"，history=[])
# print(response)
# response，history = model.chat(tokenizer，“晚上睡不着应该怎么办"，history=history)
# print(response)


#
# from transformers import AutoTokenizer, AutoModel
# tokenizer = AutoTokenizer.from_pretrained("THUDH/chatglm-6b", trust_remote_code=True)
# model = AutoModel.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True).quantize(4).half().cuda()

from transformers import AutoTokenizer, AutoModel
if __name__ == '__main__':
    # tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True)
    # model = AutoModel.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True).half().cuda()
    # response, history = model.chat(tokenizer, "你好", history=[])
    # print(response)
    # response, history = model.chat(tokenizer, "晚上睡不着应该怎么办", history=history)
    # print(response)
    pass

