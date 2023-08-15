from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/hello_world2")
def hello_world2():
    return "<h2>Sneha Is great</h2>"

@app.route("/sneha")
def sneha():
    return"<h2>I am great</h2>"

@app.route("/test1")
def test1():
    a=5+6
    return "value is {}".format(a)

@app.route("/test2/test2")
def test2():
    data= request.args.get('x')
    return "this will take input from url {}".format(data)

if __name__=="__main__":
    app.run(host="0.0.0.0")
