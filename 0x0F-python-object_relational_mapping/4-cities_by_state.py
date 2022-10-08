#!/usr/bin/python3
'''
Acript that lists all cities from the database hbtn_0e_4_usa
'''

import sys
import MySQLdb


def list_states(username, password, database_name):

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
        SELECT cities.id, cities.name, states.name FROM cities JOIN states ON\
        cities.state_id = states.id;
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
