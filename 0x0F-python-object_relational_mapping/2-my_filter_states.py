#!/usr/bin/python3
""" filter states """
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
        LIKE BINARY '{}'".format(argv[4])
    cur.execute(sql_string)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

if __name__ == "__main__":
    select_states()
