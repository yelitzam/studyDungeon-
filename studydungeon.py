from flask import Flask
from flask import render_template, flash, Markup
from flask_pymongo import PyMongo

app.config['MONGO_HOST'] = os.environ['MONGO_HOST']
app.config['MONGO_PORT'] = int(os.environ['MONGO_PORT'])
app.config['MONGO_DBNAME'] = os.environ['MONGO_DBNAME']
app.config['MONGO_URI'] = 'mongodb://studydungeon:goblin@ds237989.mlab.com:37989/studydungeon'

app = Flask(studydungeon)
mongo = PyMongo(app)

#mongo.db.events.insert_one( {"Department": dept, "Class": num,
                           #  "Name": name, "Email": contact} )

@app.route('/')
def home():
    return render_template('home.html')
