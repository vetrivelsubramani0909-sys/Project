from passlib.hash import pbkdf2_sha256
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.platypus import Table

def hash_password(password):
    return pbkdf2_sha256.hash(password)

def verify_password(password, hashed):
    return pbkdf2_sha256.verify(password, hashed)

def calculate_salary(data):
    gross = data['basic'] + data['hra'] + data['da'] + data['bonus'] + data['allowances']
    net = gross - (data['pf'] + data['tax'] + data['other_deductions'])
    return gross, net

# new funct

def emp():
    pass

def generate_payslip(employee, salary, filepath):
    doc = SimpleDocTemplate(filepath)
    elements = []
    styles = getSampleStyleSheet()

    elements.append(Paragraph(f"Payslip - {salary.month}/{salary.year}", styles['Title']))
    elements.append(Spacer(1, 12))

    data = [
        ["Employee Name", employee.name],
        ["Department", employee.department],
        ["Designation", employee.designation],
        ["Gross Salary", salary.gross_salary],
        ["Net Salary", salary.net_salary],
    ]

    table = Table(data)
    elements.append(table)
    doc.build(elements)