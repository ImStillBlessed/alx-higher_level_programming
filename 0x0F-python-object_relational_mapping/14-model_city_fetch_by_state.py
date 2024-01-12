#!/usr/bin/python3
"""Script to print all City objects from the database hbtn_0e_14_usa."""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    """
    Connect to a MySQL server running on localhost at port 3306
    Print all City objects from the database hbtn_0e_14_usa
    Results are sorted in ascending order by cities.id
    Results are displayed as <state name>: (<city id>) <city name>
    """

    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    cities = session.query(City, State).filter(City.state_id == State.id).order_by(City.id).all()

    for city, state in cities:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
