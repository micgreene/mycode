#!/usr/bin/python3
"""
Flask Mini Project | Author: Mike Greene
A simple Flask server with 2 endpoints. Returns JSON data
"""
# imports
from flask import Flask, make_response, render_template, request
import json

# Flask constructor
app = Flask(__name__)

# routes
@app.route("/")
def home():
    return render_template('./index.html')

@app.route("/page1") # this endpoint return JSON data
def page():
    # create a dict to return
    ret_dict = {
        'item1': 'one',
        'item2': 'two',
        'item3': 3,
        'item4': ['one', 2, {'key': 'value'}]
     }

    # convert it to JSON  data
    ret_dict = json.dumps(ret_dict)

    # return it
    return ret_dict

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['Name']

        resp = make_response(render_template('readcookie.html'))
        resp.set_cookie('userID', user)

    return resp

@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    msg = ""

    if name == None:
        msg = 'Please enter a name first!'
    else:
        msg = '<h1>Welcome ' + name + '</h1>'
    
    return msg

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
   # app.run(host="0.0.0.0", port=2224, debug=True) # DEBUG MODE
