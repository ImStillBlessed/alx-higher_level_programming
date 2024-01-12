#!/usr/bin/python3
"""
this is a script that lists all states and cities
from the database hbtn_0e_0_usa:
with injection protection.
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    """
    grant access to the db
    """
    db = MySQLdb.connect(host='localhost', user=argv[1], \
                         passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    state_name = argv[4]


    sql_query = "SELECT s.id, s.name, c.name \
            FROM states AS s \
            INNER JOIN cities AS c \
            ON c.state_id = s.id \
            ORDER BY s.id ASC"

    cur.execute(sql_query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    db.close()
