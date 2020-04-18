from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
class model(db.Model):
    __tablename__="model"
    Name=db.Column(db.String,primary_key=True,nullable=False)
    email=db.Column(db.String,nullable=False)
    password=db.Column(db.String,nullable=False)

def __init__(self,Name,email,password):
    self.Name=Name
    self.email=email
    self.password=password
    