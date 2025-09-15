from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("index.html")

@app.get("/login")
def login():
    return render_template("login.html")

@app.get("/register")
def register():
    return render_template("register.html")

@app.get("/rooms")
def rooms():
    return render_template("rooms.html")

@app.get("/schedule")
def schedule():
    return render_template("schedule.html")

@app.get("/bookings")
def bookings():
    return render_template("bookings.html")

@app.get("/admin")
def admin():
    return render_template("admin.html")

if __name__ == "__main__":
    app.run(debug=True)


