from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
from flask import json


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'tatanamak'

db = SQLAlchemy(app)

class user(db.Model):
    id = db.Column(db.String(80), primary_key=True)
    name = db.Column(db.String(80))
    status = db.Column(db.String(80))
    emer_contact = db.Column(db.String(20))

    def __init__(self, id,name,status,emer_contact):
       self.id = id
       self.name = name
       self.status = status
       self.emer_contact = emer_contact

@app.route('/create', methods=['GET','POST'])
def index():
    if(request.method=='POST'):
        id = name = request.form.get('uname')
        name = request.form.get('uname')
        econtact = request.form.get('econtact')
        status="safe"
        check = user.query.filter_by(id = id).first()


        app.logger.info(check)
        if(check is not None):
            return "id already exists."
        else:
            add = user(id = id, name=name, status = status, emer_contact=econtact)
            db.session.add(add)
            db.session.commit()
            return "added successfully."


@app.route('/')
def index():
    return "added successfully."
