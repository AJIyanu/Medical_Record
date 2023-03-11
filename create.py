from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

# Define the database connection URL
url = 'root:root@localhost/Medical_Record'

# Create an SQLAlchemy engine
engine = create_engine('mysql+mysqlconnector://' + url)

# Define a declarative base
Base = declarative_base()

# Define the class for your table
from models.patient import Patient
Patient()

# Create the table in the database
Base.metadata.create_all(engine)
