#!/usr/bin/python3
"""
Takes the name of the `state` as an argument
and lists all `cities` of that `state`, using the
database `hbtn_0e_4_usa`
Usage: ./4-cities_by_state.py <mysql username>
                              <mysql passwd>
                              <database name>
                              <state name>
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         port=3306,
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT cities.name
                   FROM `states`, `cities`
                   WHERE BINARY states.name = %s
                   AND cities.state_id = states.id
                   ORDER BY cities.id ASC""", [argv[4]])
    print(", ".join(state_cities[0] for state_cities in cur.fetchall()))
