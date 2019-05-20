import os
from flask import Flask, redirect

app = Flask(__name__)
messages = []

def add_message(username, message):
    messages.append("{}: {}".format(username, message))

def display_message():
    return "<br>".join(messages)

@app.route("/")
def index():
    """Intructions"""
    return "Enter your username and mesage at the end of the url /username/message"
 
@app.route("/<username>")
def user(username):
    """Display chat messages"""
    return "<h1>Welcome {}</h1>{}".format(username,display_message())
    
@app.route("/<username>/<message>")
def send_message(username, message):
    """Create a new message and redirect to the chat page"""
    add_message(username,message)
    return redirect("/" + username)
        
    
    
       

app.run(host = os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)
