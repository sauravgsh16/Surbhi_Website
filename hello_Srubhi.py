# -*- coding: utf-8 -*-
"""
Created on Thu Jul 06 20:06:17 2017

@author: user
"""

from flask import Flask, make_response, render_template
from flask_bootstrap import Bootstrap
#from flask.ext.script import Manager

app = Flask(__name__)
bootstrap = Bootstrap(app)
#manager = Manager(app)

@app.route('/')
def index():
    response = make_response('<h1>Hello Surbhi</h1>')
    response.set_cookie('answer', '42')
    return response

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
    
if __name__ == '__main__':
    app.run(debug=True)
