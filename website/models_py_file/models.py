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
    designation = db.Column(db.String(40), nullable=False, unique=False)
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

#Admission Requirements list table
class Admission_table(db.Model):
    __tablename__ = 'Admission_table'
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

#Billing Requirements list table
class Billing_table(db.Model):
    __tablename__ = 'Billing_table'
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

#Out Patient Department (OPD) Requirements list table
class OPD_table(db.Model):
    __tablename__ = 'OPD_table'
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

#In Patient Department (IPD) Requirements list table
class IPD_table(db.Model):
    __tablename__ = 'IPD_table'
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

#Radiology & Imaging Requirements list table
class Radiology_table(db.Model):
    __tablename__ = 'Radiology_table'
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

#Pathology & LIS Requirements list table
class Pathology_table(db.Model):
    __tablename__ = 'Pathology_table'
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

#Operation Theatre (OT) Management Requirements list table
class OT_table(db.Model):
    __tablename__ = 'OT_table'
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

#Emergency & Casualty Requirements list table
class Emergency_table(db.Model):
    __tablename__ = 'Emergency_table'
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

#Admin & Inventory / Med. Data Analysis Requirements list table
class Admin_table(db.Model):
    __tablename__ = 'Admin_table'
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

#EME Management Requirements list table
class EME_table(db.Model):
    __tablename__ = 'EME_table'
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

#Electronic Medical Record (EMR) Requirements list table
class EMR_table(db.Model):
    __tablename__ = 'EMR_table'
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

#Duty Management Requirements list table
class DutyManage_table(db.Model):
    __tablename__ = 'DutyManage_table'
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

#Information Desk Requirements list table
class Information_table(db.Model):
    __tablename__ = 'Information_table'
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

#Diet & Kitchen Requirements list table
class Diet_table(db.Model):
    __tablename__ = 'Diet_table'
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

#Intensive Care Unit Requirements list table
class Intensive_table(db.Model):
    __tablename__ = 'Intensive_table'
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

#Laundry Management Requirements list table
class Laundry_table(db.Model):
    __tablename__ = 'Laundry_table'
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

#Infertility Requirements list table
class Infertility_table(db.Model):
    __tablename__ = 'Infertility_table'
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

#Medical Store & Pharmacy Requirements list table
class MedicalStore_table(db.Model):
    __tablename__ = 'MedicalStore_table'
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

#Security & Access Control Requirements list table
class SecurityAccess_table(db.Model):
    __tablename__ = 'SecurityAccess_table'
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

#Connectivity Requirements list table
class Connectivity_table(db.Model):
    __tablename__ = 'Connectivity_table'
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

#Others Findings Requirements list table
class Others_table(db.Model):
    __tablename__ = 'Others_table'
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