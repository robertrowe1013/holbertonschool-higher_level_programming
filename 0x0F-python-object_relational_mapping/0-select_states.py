#!/usr/bin/python3
""" select states """
import MySQLdb
from sys import argv

def select_states():
    """ access database print states """
    db = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

if __name__ == "__main__":
    select_states()
