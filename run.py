import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    """Intructions"""
    return "Enter your username and mesage at the end of the url /username/message"
 
@app.route("/<username>")
def user(username):
    return "Hello " + username
    
@app.route("/<username>/<message>")
def show_message(username, message):
    return "{}: {}".format(username,message)
        
    
    
       

app.run(host = os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)
