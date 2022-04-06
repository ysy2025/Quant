from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success2/<name>')
def success(name):
   return 'welcome %s' % name

"""
这里的url_for指定的参数,success,是函数success,不是route的success
而login函数,是route中的login重要,而函数名称不重要
"""
@app.route('/login',methods = ['POST', 'GET'])
def login2():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(debug = True)