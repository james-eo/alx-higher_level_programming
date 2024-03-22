#!/usr/bin/python3
"""This script lists all states from the database"""

import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(user=sys.argv[1],
                           passwd=sys.argv[2],
                           database=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states")
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    conn.close()
