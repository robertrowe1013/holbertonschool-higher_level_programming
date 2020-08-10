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
    sql_string = "SELECT cities.name FROM cities \
        INNER JOIN states ON cities.state_id = states.id \
        WHERE states.name LIKE BINARY %s ORDER BY cities.id"
    cur.execute(sql_string, (argv[4],))
    rows = cur.fetchall()
    row_count = 0
    row_end = len(rows)
    if rows:
        for row in rows:
            city = str(row).strip("(')")
            city = city.replace("',", "")
            row_count += 1
            if row_count == row_end:
                print(city)
            else:
                print(city, end=", ")
    else:
        print("")
    cur.close()
    db.close()

if __name__ == "__main__":
    select_cities()
