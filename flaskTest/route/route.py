from flask import Flask
app = Flask(__name__)

"""
set FLASK_APP=hello
flask run
"""
@app.route('/hello')
def hello_world():
   return 'hello world'

if __name__ == '__main__':
    app.run(debug=True)