"""
来自客户端网页的数据作为全局请求对象发送到服务器。为了处理请求数据，应该从Flask模块导入。

Request对象的重要属性如下所列：

Form - 它是一个字典对象，包含表单参数及其值的键和值对。

args - 解析查询字符串的内容，它是问号（？）之后的URL的一部分。

Cookies  - 保存Cookie名称和值的字典对象。

files - 与上传文件有关的数据。

method - 当前请求方法。

templates,统一要在templates文件夹中!
"""


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def student():
   return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)


if __name__ == '__main__':
    print("zhangsan niubi!")

    """
    Flask 将表单数据发送到模板
    我们已经看到，可以在 URL 规则中指定 http 方法。
    触发函数接收的 Form 数据可以以字典对象的形式收集它并将其转发到模板以在相应的网页上呈现它。
    
    在以下示例中，'/' URL 会呈现具有表单的网页（student.html）。
    
    填入的数据会发布到触发 result() 函数的 '/result' URL。
    
    result() 函数收集字典对象中的 request.form 中存在的表单数据，并将其发送给 result.html。
    
    该模板动态呈现表单数据的 HTML 表格。
    """

    app.run(debug=True)