from flask import Flask, request, render_template

from config import DATABASE_URI

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine(DATABASE_URI,echo=True)
db = scoped_session(sessionmaker(bind = engine))

@app.route("/")
def index():
    airports = db.execute("SELECT * FROM airports").fetchall()
    airlines = db.execute("SELECT * FROM airlines").fetchall()
    return render_template("index.html", airports=airports, airlines=airlines)

@app.route("/check_flight", methods=["GET","POST"])
def check_flight():
    if request.method == "POST":
        origin = request.form.get("origin")
        destination = request.form.get("destination")
        airline = request.form.get("airline")

    return render_template("check_flight.html")