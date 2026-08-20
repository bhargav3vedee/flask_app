"""This is a simple Flask application that serves as a starting point 
for building web applications using the Flask framework. 
It includes a basic route that returns a greeting message when accessed."""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    """For testing purposes, this function returns a simple string."""
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True) # pragma: no cover
