# Import the dependencies.
import datetime as dt
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# when called, this function returns a date one year before the date in the arguments
def year_func(x,y,z):
    return dt.date(x,y,z) - dt.timedelta(days=365)

# when called, this function will retrieve the requested columns in the class specified in the argument
def select_var(x):
    return [x.date,
    func.min(x.tobs),
    func.max(x.tobs),
    func.avg(x.tobs)]

# when called, this function will run the query previously created through a list comprehension to create a list of dictionaries
def temp_list_func(x):
    temp_list = [{"Date": result[0], "TMIN": result[1], "TMAX": result[2], "TAVG": result[3]} for result in x]
    return temp_list

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    # home page and routes
    return (
        f"Welcome to the Climate API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/[start_date_here]<br/>"
        f"Please format start date as follows: yyyy-mm-dd<br/>"
        f"/api/v1.0/[start_date_here]/[end_date_here]<br/>"
        f"Please format start and end dates as follows: yyyy-mm-dd"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # provide the precipitation data for the previous year

    # call function to find one year before the most recent date of data
    year_ago = year_func(2017,8,23)
    # query the data for date and precipitation for all dates after the year ago date determined above
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= year_ago).all()
    # close the session
    session.close()
    # list comprehension to get a list of dictionaries including the date and precipitation
    precipitation_rows = [{"Date": result[0], "Precipitation": result[1]} for result in results]
    return jsonify(precipitation_rows)


@app.route("/api/v1.0/stations")
def stations():
    # return a list of the stations

    # query for the stations
    stations = session.query(Station.station).all()
    # close the session
    session.close()
    # list comprehension to get a list of the stations
    station_rows = [station[0] for station in stations]
    return jsonify(station_rows)


@app.route("/api/v1.0/tobs")
def tobs():
    # Return a JSON list of temperature observations for the previous year.

    # call function to find one year before the most recent date of data
    year_ago = year_func(2017,8,23)
    # query the data for date and temperature for all dates after the year ago date determined above and for a specific station
    temp_data = session.query(Measurement.date,Measurement.tobs).filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= year_ago).all()
    # close the session
    session.close()
    # list comprehension to get a list of dictionaries including the date and temperature
    tobs = [{"Date": result[0], "Temperature": result[1]} for result in temp_data]
    return jsonify(tobs)


@app.route("/api/v1.0/<start>")
def start_date(start):
    # For a specified start, calculate TMIN, TAVG, and TMAX for 
    # all the dates greater than or equal to the start date.

    # call function to create a variable to contain the data we want to select
    sel = select_var(Measurement)
    #query for the TMIN, TMAX, and TAVG for the request date and all after
    temp_query = session.query(*sel).filter(Measurement.date >= start).group_by(Measurement.date).order_by(Measurement.date).all()
    # close the session
    session.close()
    # call function to conduct list comprehension to get a list of dictionaries including the date, TMIN, TMAX, and TAVG
    return jsonify(temp_list_func(temp_query))


@app.route("/api/v1.0/<start>/<end>")
def start_and_end_date(start, end):
    # For a specified start, calculate TMIN, TAVG, and TMAX for 
    # all the dates greater than or equal to the start date.

    # call function to create a variable to contain the data we want to select
    sel = select_var(Measurement)
    #query for the TMIN, TMAX, and TAVG for the request date and all after
    temp_query = session.query(*sel).filter(Measurement.date >= start).filter(Measurement.date <= end).\
        group_by(Measurement.date).order_by(Measurement.date).all()
    # close the session
    session.close()
    # call function to conduct list comprehension to get a list of dictionaries including the date, TMIN, TMAX, and TAVG
    return jsonify(temp_list_func(temp_query))


if __name__ == "__main__":
    app.run(debug=True)