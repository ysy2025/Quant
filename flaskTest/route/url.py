from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'


@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest


@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest', guest = name))

"""
上述脚本有一个函数hello_user(name),它接受来自URL的参数的值.
这里的redirect,也是有原因的,因为两个函数设置的route是不同的
"""

if __name__ == '__main__':
   app.run(debug = True)