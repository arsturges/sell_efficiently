import os
from flask import Flask, redirect, render_template, url_for, request

app = Flask(__name__)
app.debug = True       # Set to false before deploying!

@app.route('/')
def index():
    return render_template('home.html', title = "Home") 

@app.route('/get_started', methods = ['GET','POST'])
def get_started():
    error = None
    if request.method == 'POST':
            return render_template(
                'get_started.html',
                title='Get Started',
                error = "The back end returned a parsing error. \
                        This probably means that one or more of the files \
                        you submitted isn't formatted correctly.")
    else:
        return render_template('get_started.html', title="Get Started", error=error)

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
