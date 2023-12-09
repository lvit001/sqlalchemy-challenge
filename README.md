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
