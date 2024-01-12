#!/usr/bin/python3
"""
this is a script that lists all states from state_name
from the database hbtn_0e_0_usa:

Your script should take 4 arguments: mysql username, mysql password,
database name and the state name.
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
    db = MySQLdb.connect(host='localhost', user=argv[1], \
                         passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    state_name = argv[4]
    sql_query = "SELECT id, name FROM states \
            WHERE name = {} ORDER BY states.id ASC".format(state_name)
    cur.excecute(sql_query)
    states_list = cur.fetchall()
    for state in states_list:
        print(state)
    db.close()
