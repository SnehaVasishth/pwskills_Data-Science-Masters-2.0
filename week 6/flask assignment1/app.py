from flask import Flask,url_for

app = Flask(__name__)

@app.route("/welcome")
def wel_msg():
    return "<h2>Welcome to ABC Coporation</h2>"


@app.route('/')
def company_info():
    return """
    Company Name: ABC Corporation<br>
    Location: India<br>
    Contact Detail: 999-999-9999<br>
    <a href="{}">Link to Welcome Page</a>
    """.format(url_for('wel_msg'))

# @app.route("/")
# def details():
#     return """ Company Name:ABC Coporation<br>
#     Location: India<br>
#     Contact Detail:999-999-9999
#     """
@app.route("/sneha")
def hello_world():
    return "<h1>Hello World</h1>"



if __name__=="__main__":
    app.run(host="0.0.0.0")
