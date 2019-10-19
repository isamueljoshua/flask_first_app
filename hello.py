from flask import Flask, escape
app = Flask(__name__)

# This route is to go to the index page
@app.route('/')
def index():
    return 'Index Page'

# This route is to go to hello page
@app.route('/hello')
def hello():
    return 'Hello, World'

# Varibable names in URL to make it dynamic
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

# use a converter to specify the type of the argument
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

# path - like string but also accepts slashes
@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)