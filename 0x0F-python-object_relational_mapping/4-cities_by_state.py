#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    # Default host is "localhost"
    db = MySQLdb.connect(port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()

    try:
        # Get data from database
        cursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
                        JOIN states ON cities.state_id = states.id\
                        ORDER BY cities.id ASC")
        rows = cursor.fetchall()
    except MySQLdb.Error as e:
        print("MYSQL Error: %s", str(e))

    # Print results
    for row in rows:
        print(row)
    # Close all cursors and all databases
    cursor.close()
    db.close()
