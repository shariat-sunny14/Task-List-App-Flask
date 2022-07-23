from email.policy import default
import os
from graphviz import ENGINES
from .. import db
import datetime
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy import Column, Date, Integer, DateTime



#user list table
class User(db.Model, UserMixin):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    datetime = Column(Date(), server_default=func.now())
    users_id = db.Column(db.String(20), nullable=False, unique=True)
    first_name = db.Column(db.String(20), nullable=False, unique=False)
    last_name = db.Column(db.String(20), nullable=False, unique=False)
    username = db.Column(db.String(20), nullable=False, unique=True)
    dept = db.Column(db.String(40), nullable=False, unique=False)
    email = db.Column(db.String(40), nullable=False, unique=True)
    address = db.Column(db.String(100), nullable=False, unique=False)
    mobile_number = db.Column(db.String(20), nullable=False, unique=False)
    password = db.Column(db.String(30), nullable=True)
    user_img = db.Column(db.String(200), nullable=False)

#Registration Requirements list table
class Registration_table(db.Model):
    __tablename__ = 'Registration_table'
    id = db.Column(db.Integer, primary_key=True)
    work_des = db.Column(db.String(1000), nullable=False, unique=False)
    req_by = db.Column(db.String(30), nullable=False, unique=False)
    req_type = db.Column(db.String(30), nullable=False, unique=False)
    status = db.Column(db.String(20), nullable=False, unique=False)
    priority = db.Column(db.String(20), nullable=False, unique=False)
    dev_status = db.Column(db.String(20), nullable=False, unique=False)
    qa_status = db.Column(db.String(20), nullable=False, unique=False)
    assigned_to = db.Column(db.String(30), nullable=False, unique=False)
    hours = db.Column(db.String(10), nullable=False, unique=False)
    req_date = db.Column(Date(), server_default=func.now())
    start_date = db.Column(db.String(30), nullable=False, unique=False)
    end_date = db.Column(db.String(30), nullable=False, unique=False)
    comments = db.Column(db.String(500), nullable=False, unique=False)
    referance = db.Column(db.String(50), nullable=False, unique=False)

#Prescription Requirements list table
class Prescription_table(db.Model):
    __tablename__ = 'Prescription_table'
    id = db.Column(db.Integer, primary_key=True)
    work_des = db.Column(db.String(1000), nullable=False, unique=False)
    req_by = db.Column(db.String(30), nullable=False, unique=False)
    req_type = db.Column(db.String(30), nullable=False, unique=False)
    status = db.Column(db.String(20), nullable=False, unique=False)
    priority = db.Column(db.String(20), nullable=False, unique=False)
    dev_status = db.Column(db.String(20), nullable=False, unique=False)
    qa_status = db.Column(db.String(20), nullable=False, unique=False)
    assigned_to = db.Column(db.String(30), nullable=False, unique=False)
    hours = db.Column(db.String(10), nullable=False, unique=False)
    req_date = db.Column(Date(), server_default=func.now())
    start_date = db.Column(db.String(30), nullable=False, unique=False)
    end_date = db.Column(db.String(30), nullable=False, unique=False)
    comments = db.Column(db.String(500), nullable=False, unique=False)
    referance = db.Column(db.String(500), nullable=False, unique=False)
