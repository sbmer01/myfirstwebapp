from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.dialects.postgresql import *

myapp=Flask(__name__)
myapp.config['SQLALCHEMY_DATABASE_URI']='postgres://pcexpdmejrkigm:0f79ca4d75c0344dbcaac099e1a84291baf347264951e4dd8514fec08255769d@ec2-54-225-92-1.compute-1.amazonaws.com:5432/d9gqjth7htu2mb?sslmode=require'
db=SQLAlchemy(myapp)

class Data(db.Model):
    __tablename__="entry"
    id=db.Column(db.Integer, primary_key=True)
    name_=db.Column(db.String)
    usn_=db.Column(db.Integer)
    email_=db.Column(db.String, unique=True)

    def __init__(self, name_, usn_, email_):
        self.name_=name_
        self.usn_=usn_
        self.email_=email_

@myapp.route("/")
def index():
    return render_template("index.html")

@myapp.route("/success", methods=['POST'] )
def success():
    if request.method=='POST':
        name=request.form["your_name"]
        usn=request.form["user_number"]
        email=request.form["email_add"]
        if db.session.query(Data).filter(Data.email_==email).count() == 0:
            entry=Data(name, usn, email)
            db.session.add(entry)
            db.session.commit()
            send_email(name, usn, email)
            return render_template("success.html")
    return render_template("index.html", text="That email is already listed")

if __name__ == '__main__':
    myapp.debug=True
    myapp.run()
