#!/usr/bin/python3
""" filter states with sql inj guard"""
import MySQLdb
from sys import argv


def select_states():
    """ access database print states by input """
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cur = db.cursor()
    sql_string = "SELECT * FROM states WHERE name \
        LIKE BINARY %s"
    cur.execute(sql_string, (argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

if __name__ == "__main__":
    select_states()
