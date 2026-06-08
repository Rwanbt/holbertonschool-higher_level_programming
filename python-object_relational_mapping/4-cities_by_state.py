#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa,
joining the cities and states tables.
"""

import sys

import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )

    cursor = db.cursor()

    # Jointure SQL :
    # On sélectionne cities.id, cities.name et states.name
    # On lie les tables là où cities.state_id correspond à states.id
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """

    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
