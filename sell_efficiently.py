import os
from flask import Flask, redirect, render_template, url_for, request
from contextlib import closing

app = Flask(__name__)
app.debug = True       # Set to false before deploying!
DATABASE = 'products.db'

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.route('/')
def index():
    return render_template('home.html', title = "Home") 

@app.route('/get_started', methods = ['GET','POST'])
def get_started():
    return render_template('get_started.html', title="Get Started")

@app.route('/choose_products')
def choose_products():
    return render_template('choose_products.html', title = "Choose Products") 

@app.route('/help')
def help():
    return render_template('help.html', title = "Help") 

@app.route('/about')
def about():
    return render_template('about.html', title = "About") 

@app.route('/contact')
def contact():
    return render_template('contact.html', title = "Contact") 

if __name__ == '__main__':
    app.run() #disable app.debug before pushing to production.
