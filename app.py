
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from v3toclass import getMap
DEVELOPMENT_ENV  = True

app = Flask(__name__)

app_data = {
    "name":         "ecozone",
    "description":  "",
    "author":       "ecozone Team",
    "html_title":   "",
    "project_name": "",
    "keywords":     "ecozone"
}

# from v2 import getMap

@app.route('/')
def index():
    
    return render_template('index.html', app_data=app_data)
    

@app.route('/about')
def about():
    return render_template('about.html', app_data=app_data)


@app.route('/service')
def service():
    map = getMap.getmap()
    return map._repr_html_()

    #return render_template('service.html', app_data=app_data)


@app.route('/contact')
def contact():
    return render_template('contact.html', app_data=app_data)


if __name__ == '__main__':
    app.run(debug=DEVELOPMENT_ENV)