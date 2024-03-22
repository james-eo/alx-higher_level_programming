#!/usr/bin/python3
"""This script lists all states from the database"""

import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(user="root",
                           password="MYSQL_PASSWORD",
                           database="hbtn_0e_0_usa")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states")
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    conn.close()
