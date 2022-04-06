"""
Flask Cookies
Cookie以文本文件的形式存储在客户端的计算机上。其目的是记住和跟踪与客户使用相关的数据，以获得更好的访问者体验和网站统计信息。

Request对象包含Cookie的属性。它是所有cookie变量及其对应值的字典对象，客户端已传输。除此之外，cookie还存储其网站的到期时间，路径和域名。

在Flask中，对cookie的处理步骤为：

1. 设置cookie：

    设置cookie,默认有效期是临时cookie,浏览器关闭就失效

    可以通过 max_age 设置有效期， 单位是秒

resp = make_response("success")   # 设置响应体
resp.set_cookie("w3cshool", "w3cshool", max_age=3600)

 2.获取cookie

    获取cookie，通过request.cookies的方式， 返回的是一个字典，可以获取字典里的相应的值

cookie_1 = request.cookies.get("w3cshool")

3.删除cookie

    这里的删除只是让cookie过期，并不是直接删除cookie

    删除cookie，通过delete_cookie()的方式， 里面是cookie的名字

resp = make_response("del success")  # 设置响应体
resp.delete_cookie("w3cshool")
"""

from flask import Flask, make_response, request # 注意需导入 make_response

app = Flask(__name__)

@app.route("/set_cookies")
def set_cookie():
    resp = make_response("success")
    resp.set_cookie("w3cshool", "w3cshool",max_age=3600)
    return resp

@app.route("/get_cookies")
def get_cookie():
    cookie_1 = request.cookies.get("w3cshool")  # 获取名字为Itcast_1对应cookie的值
    return cookie_1

@app.route("/delete_cookies")
def delete_cookie():
    resp = make_response("del success")
    resp.delete_cookie("w3cshool")

    return resp

if __name__ == '__main__':
    app.run(debug=True)