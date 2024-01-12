#!/usr/bin/python3
"""
this is a script that lists all states tgat start with N from the database hbtn_0e_0_usa:

Your script should take 3 arguments: mysql username, mysql password and database name
(no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    """
    grant access to the db
    """
    db = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()

    cur.execute("SELECT id, name FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id ASC")
    states_list = cur.fetchall()
    for state in states_list:
        print(state)
    db.close()
