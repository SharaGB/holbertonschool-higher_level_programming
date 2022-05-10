#!/usr/bin/python3
"""
Write Script one that is safe from MySQL injections
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    # Default host is "localhost"
    db = MySQLdb.connect(port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()

    try:
        # Get data from database
        cursor.execute("SELECT * FROM states WHERE name = %s \
                        ORDER BY states.id ASC", (argv[4],))
        rows = cursor.fetchall()
    except MySQLdb.Error as e:
        print("MYSQL Error: %s", str(e))

    # Print results
    for row in rows:
        print(row)
    # Close all cursors and all databases
    cursor.close()
    db.close()
