#!/usr/bin/python3
"""This script that lists all states with a name
starting with N (upper N) from the database
"""
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(user="root",
                           passwd="MSQL_PASSWORD",
                           db="hbtn_0e_0_usa")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%';")
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    conn.close()
