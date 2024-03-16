from flask import Flask
app = Flask(__name__)

@app.route('/')

def index():
    return 'Server Works!'

@app.route('/hello')
def hello():
    return 'Hello, greeting from different endpooint'

@app.route('/greet')
def say_hello():
    return 'Hello from Server'

@app.route('/user/<username>')
def show_user(username):
  #returns the username
  return 'Username: %s' % username
  
