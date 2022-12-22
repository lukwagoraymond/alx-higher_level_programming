#!/usr/bin/python3
"""
Lists all States objects that contain the letter `a`
Usage: ./9-model_state_filter_a.py <mysql username>
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

    result = session.query(State).filter(State.name.ilike('%a%'))\
        .order_by(State.id).all()
    for row in result:
        print("{}: {}".format(row.id, row.name))
