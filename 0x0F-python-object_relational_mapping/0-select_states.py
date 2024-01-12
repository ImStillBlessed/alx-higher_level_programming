#!/usr/bin/python3
"""
this is a script that lists all states from the database hbtn_0e_0_usa:

Your script should take 3 arguments: mysql username, mysql password and database name
(no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported
"""
import sys
import MySQLdb

if len(sys.argv) != 4:
    sys.exit(1)

username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

db = MySQLdb.connect(host='localhost', user=username, passwd=password, db=database)
cur = db.cursor()

cur.execute("SELECT id, name FROM states ORDER BY id ASC")
states = cur.fetchall()
for state in states:
    print(state)
db.close()
