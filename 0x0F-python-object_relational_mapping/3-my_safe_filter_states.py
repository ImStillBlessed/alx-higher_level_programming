#!/usr/bin/python3
"""
this is a script that lists all states with state_name
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
    sql_query = "SELECT id, name FROM states WHERE name = %s ORDER BY states.id ASC"
    cur.excecute(sql_query, (state_name,))
    states_list = cur.fetchall()
    for state in states_list:
        print(state)
    db.close()
