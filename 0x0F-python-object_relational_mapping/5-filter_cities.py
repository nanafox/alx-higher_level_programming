#!/usr/bin/python3

"""This script lists all cities from the database `hbtn_0e_4_usa`"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    username, password, db_name, state_name = sys.argv[1:]

    conn = MySQLdb.connect(
        host="localhost",
        user=username,
        password=password,
        database=db_name,
        port=3306,
    )

    cursor = conn.cursor()

    # The query is modified to filter the cities by state name
    cursor.execute(
        """
        SELECT cities.name
        FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
        ORDER BY cities.id;
        """,
        (state_name,),
    )

    result_set = cursor.fetchall()

    print(", ".join(row[0] for row in result_set))

    cursor.close()
    conn.close()
