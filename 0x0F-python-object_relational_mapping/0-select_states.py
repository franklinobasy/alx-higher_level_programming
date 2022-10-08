#!/usr/bin/python3
'''Script that lists all states from database hbtn_0e_0_usa
'''

import MySQLdb
import sys


def list_states(username, password, database_name):
    '''This functions prints all states in the database'''

    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database_name,
        charset="utf8",
    )

    cursor = connection.cursor()

    query = '''
        SELECT * FROM states ORDER BY states.id ASC;
    '''

    cursor.execute(query)

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    connection.close()


if __name__ == "__main__":
    argv = sys.argv[1:]
    username, password, db_name = argv
    list_states(username, password, db_name)
