from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Employee Salary System Running"

if __name__ == "__main__":
    print("Server Starting...")
    app.run(debug=True)