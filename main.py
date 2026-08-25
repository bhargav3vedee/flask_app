"""This is a simple Flask application that serves as a starting point 
for building web applications using the Flask framework. 
It includes a basic route that returns a greeting message when accessed."""

import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    """For testing purposes, this function returns a simple string."""
    return "Hello, World!"

@app.route('/health')
def health_check():
    """Health check endpoint to verify that the application is running."""
    return "OK"

if __name__ == '__main__':
    with open("flask.pid", "w") as f:
        f.write(str(os.getpid()))
    app.run(debug=True, host='0.0.0.0', port=8000) # pragma: no cover
