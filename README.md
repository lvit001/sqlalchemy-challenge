# sqlalchemy-challenge: Module 10 Challenge
## [Part 1: Climate Starter Jupyter Notebook](https://github.com/lvit001/sqlalchemy-challenge/blob/main/SurfsUp/climate_starter.ipynb)
### Reflect Tables into SQLAlchemy ORM
- Used `Base = automap_base()` and `Base.prepare(autoload_with=engine)` to reflect the hawaii.sqlite database and tables
- Used `Base.classes.keys()` to determine the classes found in the reflected database
- Used `Measurement = Base.classes.measurement` and `Station = Base.classes.station` to create references to the classes in the database
- Used `session = Session(engine)` to create the link between Python and the database
### Exploratory Precipitation Analysis
- Created a query to find the most recent date in the data set: `most_recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()`
- Found the date one year before the most recent date in the data set: `year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)`
- Performed a query to retrieve date and precipitation data for the most recent year in the data set: `precipitation_data = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= year_ago).all()`
- Create a dataframe with the data retrieved from the query and renamed the columns: `df = pd.DataFrame(precipitation_data, columns=["Date","Precipitation"])`
- Organized the dataframe and set the index to the date: df = `df.sort_values(by="Date",ascending=True)` & `df.set_index(df["Date"], inplace=True)`
- Created a pandas plot with the data:
- `df.plot(color='m')`
- `plt.tight_layout()`
- `plt.xticks(rotation='vertical')`
- `plt.xlabel("Date")`
- `plt.ylabel("Inches")`
- `plt.show()`
- Created the below graph displaying precipitation data over time:
- ![image](https://github.com/lvit001/sqlalchemy-challenge/assets/140283164/fb19015b-e883-4202-b550-6c4853692b70)
- Calculated a summary statistics table for the data `df.describe()`
### Exploratory Station Analysis
- Created a query to calculate the number of stations: `number_stations = session.query(func.count(Station.station)).all()`
- Created a query to list the active stations and how many rows of data they had, sorted from highest to lowest: `most_active_stations = session.query(Measurement.station, func.count(Measurement.station)).group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).all()`
- Performed a quey to find the min, max, and avg temps for the most active station:
- `sel = [func.min(Measurement.tobs),func.max(Measurement.tobs),func.avg(Measurement.tobs)]`
- `most_active_temps = session.query(*sel).filter(Measurement.station == 'USC00519281').first()`
- Designed a query to find the tobs over the last year for the most active station, and graphed this data in a histogram:
- `temp_data = session.query(Measurement.date,Measurement.tobs).filter(Measurement.station == 'USC00519281').filter(Measurement.date >= year_ago).all()`
- `df = pd.DataFrame(temp_data)`
- `df.plot.hist(bins=12, color='m')`
- `plt.xlabel('Temperature')`
- `plt.ylabel("Frequency")`
- Populated the below histogram graph:
- ![image](https://github.com/lvit001/sqlalchemy-challenge/assets/140283164/1dc2a296-945b-4a43-be43-05a5ff42e020)
### Close Session
- Used `session.close()` to close the session
## Part 2: Climate API Development
###
