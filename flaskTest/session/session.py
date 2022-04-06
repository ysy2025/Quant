"""
Flask Sessions（会话）
与Cookie不同，Session（会话）数据存储在服务器上。
会话是客户端登录到服务器并注销服务器的时间间隔。需要在该会话中保存的数据会存储在服务器上的临时目录中。

为每个客户端的会话分配会话ID。会话数据存储在cookie的顶部，服务器以加密方式对其进行签名。
对于此加密，Flask应用程序需要一个定义的SECRET_KEY。

Session对象也是一个字典对象，包含会话变量和关联值的键值对。

例如，要设置一个'username'会话变量，请使用以下语句：

Session['username'] = 'admin'
要释放会话变量，请使用pop()方法。

session.pop('username', None)
"""

from flask import render_template

from flask import make_response

from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)
app.secret_key = 'any random string'

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return 'Logged in as ' + username + '<br>'  \
         "<b><a href = '/logout'>click here to log out</a></b>"

    """
    一开始是没有session的,所以会返回,click here to log in ...
    等有了session之后,
    """
    return """
    You are not logged in <br><a href = '/login'></b>
    click here to log in</b></a>"""


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''

   <form action = "" method = "post">
      <p><input type="text" name="username"/></p>
      <p<<input type="submit" value="Login"/></p>
   </form>

   '''

@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)