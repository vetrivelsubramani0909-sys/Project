from flask import Blueprint, request, jsonify
from extensions import db
from models import Salary, Employee
from utils import calculate_salary, generate_payslip
from flask_jwt_extended import jwt_required

salary_bp = Blueprint('salary', __name__)

@salary_bp.route('/salary', methods=['POST'])
@jwt_required()
def add_salary():
    data = request.json
    gross, net = calculate_salary(data)

    salary = Salary(
        employee_id=data['employee_id'],
        month=data['month'],
        year=data['year'],
        basic=data['basic'],
        hra=data['hra'],
        da=data['da'],
        bonus=data['bonus'],
        allowances=data['allowances'],
        pf=data['pf'],
        tax=data['tax'],
        other_deductions=data['other_deductions'],
        gross_salary=gross,
        net_salary=net
    )

    db.session.add(salary)
    db.session.commit()
    return jsonify({"message": "Salary processed"})