from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Shelter, Puppy

engine = create_engine('sqlite:///puppyrescue.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

for i in range(0,5):
	shelter = Shelter(name = "No" + str(i+2) +  "Shelter")
	session.add(shelter)

	puppy = Puppy(name="doggy"+str(i+1), gender ="male", dob=str(i)+" month(s) before",shelter=shelter)
	session.add(puppy)
session.commit()

