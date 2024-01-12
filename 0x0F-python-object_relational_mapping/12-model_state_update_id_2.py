#!/usr/bin/python3
"""
This script changes the name of a State object
from the database hbtn_0e_6_usa.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and get a state
    from the database.
    """

    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    state_replace = session.query(State).filter(State.id == 2).first()
    if state_replace:
        state_replace.name = 'New Mexico'
        session.commit()