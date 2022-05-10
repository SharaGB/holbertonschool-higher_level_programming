#!/usr/bin/python3
"""
Takes in the name of a state as an argument and lists all cities
    of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    # Default host is "localhost"
    db = MySQLdb.connect(port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()

    try:
        # Get data from database
        cursor.execute("SELECT cities.name FROM cities\
                        JOIN states ON cities.state_id = states.id\
                        WHERE states.name = %s\
                        ORDER BY cities.id ASC", (argv[4],))
        rows = cursor.fetchall()
    except MySQLdb.Error as e:
        print("MYSQL Error: %s", str(e))

    # Print results
    print(', '.join(row[0] for row in rows))
    # Close all cursors and all databases
    cursor.close()
    db.close()
