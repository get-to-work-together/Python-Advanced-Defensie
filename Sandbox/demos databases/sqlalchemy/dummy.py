import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from tabledef import *

engine = create_engine('sqlite:///student.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

# Create objects
user = Student("arthur","Arthur","Boogie","MIT")
session.add(user)

user = Student("nick","Nick","Miami","UVA")
session.add(user)

user = Student("peter","Peter","Anema","TU Delft")
session.add(user)

# commit the record the database
session.commit()