import os
from flask import Flask, redirect, render_template, url_for, request
from contextlib import closing
from sqlite3 import dbapi2 as sqlite3

app = Flask(__name__)
app.debug = False # Set to false before deploying!
DATABASE = 'products.sqlite3'
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.route('/')
def index():
    return render_template('home.html', title = "Home")

@app.route('/view_results', methods=['GET','POST'])
def view_results():
    results_visibility = 'block'
    pic_urls = {}
    pic_urls['Small'] = 'http://images.lowes.com/product/converted/036725/036725568419.jpg'
    pic_urls['Medium'] = 'http://images.lowes.com/product/converted/883049/883049181479.jpg'
    pic_urls['Large'] = 'http://images.lowes.com/product/converted/012505/012505698699.jpg'
    pic_url_1 = pic_urls[request.form['size1']]
    pic_url_2 = pic_urls[request.form['size2']]
    product1_sql = "select * from products where modelNumber = 'KDDC24CVS'"
    product2_sql = "select * from products where modelNumber = 'RF263AEWP'"

    db = connect_db()
    fridge1 = db.execute(product1_sql)
    fridge2 = db.execute(product2_sql)
    fridge1_attributes = []
    for row in fridge1.fetchall():
        fridge1_attributes.append(row)
    fridge2_attributes = []
    for row in fridge2.fetchall():
        fridge2_attributes.append(row)

    return render_template('view_results.html', 
      title="Product Comparison Results", 
      pic_url_1=pic_url_1,
      pic_url_2=pic_url_2,
      results_visibility=results_visibility,
      results1=fridge1_attributes,
      results2=fridge2_attributes)

@app.route('/choose_products', methods=['GET','POST'])
def choose_products():
      results_visibility = 'none'
      db = connect_db()

      brands = db.execute('select distinct(brandName) from products order by type asc')
      list_of_brands = []
      for row in brands.fetchall():
          list_of_brands.append(row)

      types = db.execute('select distinct(type) from products order by type asc')
      list_of_types = []
      for row in types.fetchall():
          list_of_types.append(row)

      sizes = db.execute('select distinct(sizeSort) from products order by sizeSort desc')
      list_of_sizes = []
      for row in sizes.fetchall():
          list_of_sizes.append(row)

      return render_template('choose_products.html', title = "Choose Products", 
        brands=list_of_brands,
        types = list_of_types,
        sizes = list_of_sizes,
        results_visibility = results_visibility,
        results1=None,
        results2=None) 

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
