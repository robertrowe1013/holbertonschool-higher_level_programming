#!/usr/bin/python3
""" cities by state """
import MySQLdb
from sys import argv


def select_cities():
    """ access database print states by input """
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cur = db.cursor()
    sql_string = "SELECT cities.id, cities.name, states.name FROM cities \
        INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id"
    cur.execute(sql_string)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

if __name__ == "__main__":
    select_cities()
