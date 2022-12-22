#!/usr/bin/python3
"""
Lists First `State` Objects from the database `hbtn_0e_6_usa`
Usage: ./7-model_state_fetch_all <mysql username>
                                 <mysql password>
                                 <database name>
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

    for row in session.query(State.id, State.name).filter(State.id == '1'):
        print("{}: {}".format(row.id, row.name))
