#!/usr/bin/python3
"""
Lists all cities from the database `hbtn_0e_4_usa`
Usage: ./4-cities_by_state.py <mysql username>
                              <mysql passwd>
                              <database name>
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
    cur.execute("""SELECT cities.id, cities.name, states.name
                   FROM `states`, `cities`
                   WHERE cities.state_id = states.id
                   ORDER BY cities.id ASC""")
    [print(state) for state in cur.fetchall()]
