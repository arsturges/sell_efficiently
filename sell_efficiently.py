import os
from flask import Flask, redirect, render_template, url_for, request
from contextlib import closing
from sqlite3 import dbapi2 as sqlite3

app = Flask(__name__)
app.debug = True       # Set to false before deploying!
DATABASE = 'products.sqlite3'
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])
"""
@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    g.db.close()
"""

@app.route('/')
def index():
    return render_template('home.html', title = "Home") 

@app.route('/get_started')
def get_started():
    return render_template('get_started.html', title="Get Started")

@app.route('/choose_products')
def choose_products():
    db = connect_db()
    brands = db.execute('select distinct(brandName) from products order by type asc')
    list_of_brands = []
    for row in brands.fetchall():
        list_of_brands.append(row)
    types = db.execute('select distinct(type) from products order by type asc')
    list_of_types = []
    for row in types.fetchall():
        list_of_types.append(row)
    return render_template('choose_products.html', title = "Choose Products", 
      brands=list_of_brands,
      types = list_of_types) 

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
