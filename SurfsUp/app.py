# Import the dependencies.
from flask import Flask, jsonify
from sqlalchemy import func

from sqlalchemy import create_engine,inspect 
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session


#################################################
# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
#################################################


# reflect an existing database into a new model
Base = automap_base()
Base.prepare(engine,reflect=True)
# reflect the tables
Inspector = inspect(engine)
tablenames= Inspector.get_table_names()



# Save references to each table
Class_Station = Base.classes.station
Class_Measurement = Base.classes.measurement

# Create our session (link) from Python to the DB
session_link = Session(engine)

#################################################
# Flask Setup
#################################################




#################################################
# Flask Routes
#################################################
# 2. Create an app

app = Flask(__name__)
#page listing the available route 

@app.route("/")
def home():
   
    return(
        "Welcome to the Climate Flask API<br/>"
        "Available Route:<br/>"
        "/api/v1.0/precipitation<br/>"
        "/api/v1.0/stations<br/>"
        "/api/v1.0/tobs<br/>"
        "/api/v1.0/start<br/>"
        "/api/v1.0/start/end"

    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    Precipitation_data=session_link.query(Class_Measurement.date,Class_Measurement.prcp).\
    filter(Class_Measurement.date >'2016-08-23').\
    order_by(Class_Measurement.date.desc()).all()
    Precipitation_dict = {}
    for date,prcp in Precipitation_data:
        Precipitation_dict[date]=prcp 
    return jsonify(Precipitation_dict)      
    


@app.route("/api/v1.0/stations")
def stations():
    results = session_link.query(Class_Station.station).all()
    station_list = [] 
    for station,in results:
        station_list.append(station)
    return jsonify(station_list)
@app.route("/api/v1.0/tobs")
def tobs():

    Temperature_data=session_link.query(Class_Measurement.date,Class_Measurement.tobs).\
    filter(Class_Measurement.date >'2016-08-23').\
    order_by(Class_Measurement.date.desc()).all()
    tobs_list = []
    for date, tobs in Temperature_data:
        tobs_list.append({"date":date,"Temperature":tobs})
    return jsonify(tobs_list)

@app.route("/api/v1.0/start")
def start():
    Temperature_details = session_link.query(func.min(Class_Measurement.tobs),func.max(Class_Measurement.tobs),func.avg(Class_Measurement.tobs)).\
    filter(Class_Measurement.date >= '2016-08-23').all()
    temperature_dict={"min_temp":Temperature_details[0][0],"max_temp":Temperature_details[0][1],"avg_temp":Temperature_details[0][2]}
    return jsonify(temperature_dict)

@app.route("/api/v1.0/start/end")
def start_end():
    start = "2016-08-23"
    end = "2016-12-31"
    Temperature_details = session_link.query(func.min(Class_Measurement.tobs),func.max(Class_Measurement.tobs),func.avg(Class_Measurement.tobs)).\
    filter(Class_Measurement.date >= start,Class_Measurement.date <= end).all()
    temperature_dict={"min_temp":Temperature_details[0][0],"max_temp":Temperature_details[0][1],"avg_temp":Temperature_details[0][2]}
    return jsonify(temperature_dict)



if __name__ == "__main__":
    app.run(debug=True)