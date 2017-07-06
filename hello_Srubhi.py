# -*- coding: utf-8 -*-
"""
Created on Thu Jul 06 20:06:17 2017

@author: user
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello Surbhi</h1>'
    
if __name__ == '__main__':
    app.run(debug=True)

