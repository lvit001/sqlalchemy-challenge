# sqlalchemy-challenge: Module 10 Challenge
## [Part 1: Climate Starter Jupyter Notebook](https://github.com/lvit001/sqlalchemy-challenge/blob/main/SurfsUp/climate_starter.ipynb)
### Reflect Tables into SQLAlchemy ORM
- Used `Base = automap_base()` and `Base.prepare(autoload_with=engine)` to reflect the hawaii.sqlite database and tables
- Used `Base.classes.keys()` to determine the classes found in the reflected database
- Used `Measurement = Base.classes.measurement` and `Station = Base.classes.station` to create references to the classes in the database
- Used `session = Session(engine)` to create the link between Python and the database
### Exploratory Precipitation Analysis
- 
