import os

from flask import Flask, session,request,render_template,redirect
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from model import *

app = Flask(__name__)
# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

app.config["SQLALCHEMY_DATABASE_URI"]=os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False


# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
db.init_app(app)
# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
Session = scoped_session(sessionmaker(bind=engine))
session = Session()

# db = scoped_session(sessionmaker(bind=engine))



@app.route("/")
def index():
    return render_template("registration.html")
    
@app.route("/form",methods=["POST","GET"])
def form():
    db.create_all()
    if request.method=="GET":
        return render_template("registration.html")
    else:
        udata=model(request.form["Name"],request.form["email"],request.form["password"])
        # Name=request.form.get("Name")
        # email=request.form.get("email")
        #password=request.get.form("password")
        db.session.add(udata)
        db.session.commit()
        # return render_template("form.html",Name=Name,email=email,password=password)
        return render_template("registration.html")