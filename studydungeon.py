from __future__ import print_function
from flask import Flask, redirect, url_for, session, request, jsonify
from flask import render_template, flash, Markup
from flask import session
from flask_pymongo import PyMongo
from github import Github

import os

app = Flask(__name__)
app.debug = False
app.secret_key = os.environ['APP_SECRET_KEY']

app.config['MONGO_HOST'] = os.environ['MONGO_HOST']
app.config['MONGO_PORT'] = int(os.environ['MONGO_PORT'])
app.config['MONGO_DBNAME'] = os.environ['MONGO_DBNAME']
app.config['MONGO_USERNAME'] = os.environ['MONGO_USERNAME']
app.config['MONGO_PASSWORD'] = os.environ['MONGO_PASSWORD']

mongo = PyMongo(app)

@app.route('/')
def home():

    return render_template('home.html')

@app.route('/list')
def render_list():
    try:
        dept = str(request.args['department'])
        num = int(request.args['number'])
        buddies = []
        mail = []
        for buddy in mongo.db.events.find({ "Department": dept, "Class": num }):
            person = buddy["Name"]
            buddies.append(person)
            cont = buddy["Email"]
            mail.append(cont)
        return render_template('list.html', buds = buddies, emails = mail, dept = dept, num = num)
    except ValueError:
        return "Sorry: something went wrong."
    
@app.route('/added')
def render_added():
    try:
        dept = str(request.args['department'])
        num = int(request.args['number'])
        name = str(request.args['name'])
        email = str(request.args['email'])
        toMail = []
        for person in mongo.db.events.find({ "Department": dept, "Class": num }):
            cont = person["Email"]
            mail.append(cont)
        mongo.db.events.insert_one( {"Department": dept, "Class": num, "Name": name, "Email": email} )
        return render_template('added.html', list = toMail)
    except ValueError:
        return "Sorry: something went wrong."
    
@app.route('/about')
def render_about():
    return render_template('about.html')

if __name__=="__main__":
    app.run(debug=False, port=5000)
