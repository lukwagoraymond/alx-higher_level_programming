#!/usr/bin/python3
"""
Change name of `State` object in database `hbtn_0e_6_usa`
Usage: ./12-mode_state_update_id_2.py <mysql username>
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

    result = session.query(State).filter_by(id=2).first()
    result.name = 'New Mexico'
    session.commit()
