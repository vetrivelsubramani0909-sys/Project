from flask import Blueprint, jsonify
from models import Salary
from flask_jwt_extended import jwt_required

report_bp = Blueprint('report', __name__)

@report_bp.route('/report/<int:month>/<int:year>', methods=['GET'])
@jwt_required()
def salary_report(month, year):
    salaries = Salary.query.filter_by(month=month, year=year).all()
    return jsonify([{
        "employee_id": s.employee_id,
        "gross": s.gross_salary,
        "net": s.net_salary
    } for s in salaries])