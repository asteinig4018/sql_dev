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
    cities = list()
    #create list of just cities
    cities = [ i[2] for i in airports]
    #take out doubles
    cities = list(set(cities))
    return render_template("index.html", cities=cities, airlines=airlines)

@app.route("/check_flight", methods=["GET","POST"])
def check_flight():
    if request.method == "POST":
        origin_city = request.form.get("origin")
        destination_city = request.form.get("destination")
        airline = request.form.get("airline")

        #first, remap city to airport

        #get list of origin airport ids

        origins = db.execute(f"SELECT id, name, city, country, iata_code, icao_code FROM airports WHERE city = '{origin_city}'").fetchall()
        
        origins_id = [ i[0] for i in origins]
        origins_id_str = "("
        for origin_id in origins_id:
            origins_id_str += "'"
            origins_id_str += str(origin_id)
            origins_id_str += "',"
        origins_id_str = origins_id_str[:-1]
        origins_id_str += ")"

        #get list of destination airport ids    

        destinations = db.execute(f"SELECT id, name, city, country, iata_code, icao_code FROM airports WHERE city = '{destination_city}'").fetchall()
        destinations_id = [ i[0] for i in destinations]
        destinations_id_str = "("
        for origin_id in destinations_id:
            destinations_id_str += "'"
            destinations_id_str += str(origin_id)
            destinations_id_str += "',"
        destinations_id_str = destinations_id_str[:-1]
        destinations_id_str += ")"

        #search routes table by airports
        routes = db.execute(f"SELECT * FROM routes WHERE source_airport_id IN {origins_id_str} AND destination_airport_id IN {destinations_id_str}").fetchall()

    return render_template("check_flight.html", routes=routes)