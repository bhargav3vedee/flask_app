from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello world"

@app.route('/index')
def index():
    return "Hello from index page"

if __name__ == '__main__':
    app.run(debug=True)
