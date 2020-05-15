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
        #get list of ids
        routes_airline_id = [i[2] for i in routes]
        #create string to query
        routes_airline_id_str= "("+ str(routes_airline_id)[1:-1] +")"
        #query database and receive mapping to limit database queries to one
        airline_names = db.execute(f"SELECT ofid,name FROM airlines WHERE ofid IN {routes_airline_id_str}").fetchall()
        ofid_list = [i[0] for i in airline_names]
        name_list = [i[1] for i in airline_names]
        routes_airline_names = list()
        for airline_id in routes_airline_id:
            routes_airline_names.append(name_list[ofid_list.index(airline_id)])

        route_data_packet = zip(routes,routes_airline_names)

    return render_template("check_flight.html", route_data_packet=route_data_packet, origin_city=origin_city, destination_city=destination_city)


@app.route("/routes/<int:route_id>", methods=["GET"])
def routes(route_id):
    #get route info
    route_info = db.execute(f"SELECT * FROM routes WHERE id={route_id}").fetchall()
    #extract airline id
    airline_id = str([i[2] for i in route_info])[1:-1]
    #get airine info
    airline_info = db.execute(f"SELECT * FROM airlines WHERE ofid = {airline_id}").fetchall()
    airline_name = str([i[2] for i in airline_info])[2:-2]
    #extract plane/equipment id
    plane_id = str([i[9] for i in route_info])[2:-2].split()
    #get plane info
    plane_info = list()
    for pid in plane_id:
        plane_info.append(db.execute(f"SELECT * FROM planes WHERE iata_code = '{pid}'").fetchall())
    #extract source and destination airport id
    source_airport_id = str([i[4] for i in route_info])[1:-1]
    destination_airport_id = str([i[6] for i in route_info])[1:-1]
    #get airport info
    source_airport_info = db.execute(f"SELECT * FROM airports WHERE id = {source_airport_id}").fetchall()
    destination_airport_info = db.execute(f"SELECT * FROM airports WHERE id = {destination_airport_id}").fetchall()

    origin_city = str([i[2] for i in source_airport_info])[2:-2] + ", " + str([i[3] for i in source_airport_info])[2:-2]
    origin_airport = str([i[1] for i in source_airport_info])[2:-2]

    destination_city = str([i[2] for i in destination_airport_info])[2:-2] + ", " + str([i[3] for i in destination_airport_info])[2:-2]
    destination_airport = str([i[1] for i in destination_airport_info])[2:-2]    

    plane = ""
    for plane_i in plane_info:
        plane += str([i[1] for i in plane_i])[2:-2] +", "
    plane = plane[:-2]  

    return render_template("route_info.html", route_id=route_id, airline_name=airline_name, origin_airport=origin_airport, origin_city=origin_city, destination_airport=destination_airport, destination_city=destination_city, plane=plane)
