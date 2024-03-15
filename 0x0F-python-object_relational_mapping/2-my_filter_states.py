#!/usr/bin/python3

"""This script takes in an argument and displays all values in the `states`
table of the database `hbtn_0e_0_usa` where the `name` matches the argument."""

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

    # The query is written in a way that is unsafe from SQL injection
    query = """
        SELECT * FROM states
        WHERE name LIKE BINARY '{}'
        ORDER BY states.id;
    """.format(state_name)

    cursor.execute(query)

    result_set = cursor.fetchall()

    for row in result_set:
        print(row)

    cursor.close()
    conn.close()
