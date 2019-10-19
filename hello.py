from flask import Flask
app = Flask(__name__)

# This route is to go to the index page
@app.route('/')
def index():
    return 'Index Page'

# This route is to go to hello page
@app.route('/hello')
def hello():
    return 'Hello, World'