#!/usr/bin/python3
"""
Lists all `Cities` Objects from the database `hbtn_0e_14_usa`
Usage: ./14-model_city_fetch_by_state.py <mysql username>
                                         <mysql password>
                                         <database name>
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State, City).filter(State.id == City.state_id).all()
    for state, city in result:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
