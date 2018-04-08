from __future__ import print_function
from flask import Flask, redirect, url_for, session, request, jsonify
from flask_oauthlib.client import OAuth
from flask import render_template, flash, Markup
from flask import session
from flask_pymongo import PyMongo
from github import Github

class GithubOAuthVarsNotDefined(Exception):
    '''raise this if the necessary env variables are not defined '''

if os.getenv('GITHUB_CLIENT_ID') == None or \
        os.getenv('GITHUB_CLIENT_SECRET') == None or \
        os.getenv('APP_SECRET_KEY') == None or \
        os.getenv('GITHUB_ORG') == None:
    raise GithubOAuthVarsNotDefined('''
      Please define environment variables:
         GITHUB_CLIENT_ID
         GITHUB_CLIENT_SECRET
         GITHUB_ORG
         APP_SECRET_KEY
      ''')

app = Flask(__name__)
app.debug = False
app.secret_key = os.environ['APP_SECRET_KEY']

app.config['MONGO_HOST'] = os.environ['MONGO_HOST']
app.config['MONGO_PORT'] = int(os.environ['MONGO_PORT'])
app.config['MONGO_DBNAME'] = os.environ['MONGO_DBNAME']
app.config['MONGO_USERNAME'] = os.environ['MONGO_USERNAME']
app.config['MONGO_PASSWORD'] = os.environ['MONGO_PASSWORD']
app.config['MONGO_URI'] = 'mongodb://studydungeon:goblin@ds237989.mlab.com:37989/studydungeon'

mongo = PyMongo(app)

@github.tokengetter
def get_github_oauth_token():
    return session.get('github_token')

@app.context_processor
def inject_logged_in():
    return dict(logged_in=('github_token' in session))

@app.context_processor
def inject_github_org():
    return dict(github_org=os.getenv('GITHUB_ORG'))

app.secret_key='w98fw9ef8hwe98fhwef'

#mongo.db.events.insert_one( {"Department": dept, "Class": num,
                           #  "Name": name, "Email": contact} )

@app.route('/')
def home():
    return render_template('home.html')
