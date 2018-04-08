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
#app.config['MONGO_URI'] = 'mongodb://studydungeon:goblin@ds237989.mlab.com:37989/studydungeon'

mongo = PyMongo(app)


#app.secret_key='w98fw9ef8hwe98fhwef'

#mongo.db.events.insert_one( {"Department": dept, "Class": num,
                           #  "Name": name, "Email": contact} )

@app.route('/')
def home():
    return render_template('home.html')


if __name__=="__main__":
    app.run(debug=False, port=5000)
