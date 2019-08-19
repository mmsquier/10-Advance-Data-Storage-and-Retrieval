
from matplotlib import style
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as dt
from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

app= Flask(__name__)

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# We can view all of the classes that automap found
Base.classes.keys()

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

@app.route('/')
def home ():
    return (f'I work')

@app.route('/api/v1.0/precipitation')
def precipitation():
    session=Session(engine)
    results=session.query(Measurement.date, Measurement.prcp).\
            order_by(Measurement.date.desc()).all()
    my_dict = [{result[0]:result[1]} for result in results]

    return jsonify(my_dict)

@app.route('/api/v1.0/station')
def station():
    session=Session(engine)
    results=session.query(Station.name).\
            order_by(Measurement.date.desc()).all()
    my_dict = [{result[0]:result[1]} for result in results]

    return jsonify(my_dict)


if __name__=="__main__":
    app.run()