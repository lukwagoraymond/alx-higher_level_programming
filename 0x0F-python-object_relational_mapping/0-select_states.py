#!/usr/bin/python3
"""
Script that Lists all `states` from the database `hbtn_0e_0_usa`
Usage: ./0-select_states.py <mysql username>
                            <mysql passwd>
                            <database name>
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], port=3306, passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states` ORDER BY states.id ASC")
    [print(state) for state in c.fetchall()]
