#!/usr/bin/python3
"""
Takes an argument and displays all values in the states table
    of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    # Default host is "localhost"
    db = MySQLdb.connect(port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()

    try:
        # Get data from database
        cursor.execute("SELECT * FROM states WHERE name = '{}'\
                        ORDER BY states.id ASC".format(argv[4]))
        rows = cursor.fetchall()
    except MySQLdb.Error as e:
        print("MYSQL Error: %s", str(e))

    # Print results
    for row in rows:
        if row[1] == argv[4]:
            print(row)
    # Close all cursors and all databases
    cursor.close()
    db.close()
