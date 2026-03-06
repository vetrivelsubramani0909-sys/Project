from extensions import db
from datetime import datetime

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    dob = db.Column(db.Date)
    email = db.Column(db.String(120), unique=True)
    phone = db.Column(db.String(20))
    address = db.Column(db.Text)
    department = db.Column(db.String(100))
    designation = db.Column(db.String(100))
    joining_date = db.Column(db.Date)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Salary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    month = db.Column(db.Integer)
    year = db.Column(db.Integer)

    basic = db.Column(db.Float)
    hra = db.Column(db.Float)
    da = db.Column(db.Float)
    bonus = db.Column(db.Float)
    allowances = db.Column(db.Float)

    pf = db.Column(db.Float)
    tax = db.Column(db.Float)
    other_deductions = db.Column(db.Float)

    gross_salary = db.Column(db.Float)
    net_salary = db.Column(db.Float)

    employee = db.relationship('Employee', backref='salaries')