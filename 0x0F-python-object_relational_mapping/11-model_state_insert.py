#!/usr/bin/python3
"""
Prints `State` object with the `name` passed as
argument from the database `hbtn_0e_6_usa`
Usage: ./10-mode_state_my_get.py <mysql username>
                                 <mysql password>
                                 <database name>
                                 <name searched>
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    newState = State(name='Louisiana')
    session.add(newState)
    session.commit()
    result = session.query(State).filter_by(name='Louisiana').first()
    print("{}".format(result.id))
