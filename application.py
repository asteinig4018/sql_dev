from flask import Flask, request, render_template

#from config import DATABASE_URI

#from sqlalchemy import create_engine
#from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

#engine = create_engine(DATABASE_URI,echo=True)
#db = scoped_session(sessionmaker(bind = engine))

@app.route("/")
def index():
    origins = list()
    destinations = list()
    airlines = list()
    return render_template("index.html", origins=origins, destinations=destinations, airlines=airlines)

@app.route("/check_flight", methods=["GET","POST"])
def check_flight():
    pass