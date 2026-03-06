from flask import Blueprint, request, jsonify
from extensions import db
from models import Employee
from flask_jwt_extended import jwt_required

employee_bp = Blueprint('employee', __name__)

@employee_bp.route('/employees', methods=['POST'])
@jwt_required()
def add_employee():
    data = request.json
    emp = Employee(**data)
    db.session.add(emp)
    db.session.commit()
    return jsonify({"message": "Employee added"})

@employee_bp.route('/employees', methods=['GET'])
@jwt_required()
def get_employees():
    employees = Employee.query.all()
    return jsonify([{
        "id": e.id,
        "name": e.name,
        "email": e.email
    } for e in employees])