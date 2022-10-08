#!/usr/bin/python3
'''
A script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa
'''

import sys
import MySQLdb


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
        SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC;
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
