#!/usr/bin/python3
'''
a script that takes in the name of a state as
an argument and lists all cities of that state,
using the database hbtn_0e_4_usa
'''

import sys
import MySQLdb


def list_states(username, password, database_name, argument):

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
            SELECT cities.name FROM cities\
            INNER JOIN states ON cities.state_id = states.id\
            WHERE states.name = %s \
            ORDER BY cities.id ASC
        '''

    cursor.execute(query.format(argument), (argument,))

    results = cursor.fetchall()

    for i in range(len(results)):
        print(results[i][0], end="\n" if i == len(results) - 1 else ", ")

    cursor.close()
    connection.close()


if __name__ == "__main__":
    argv = sys.argv[1:]
    username, password, db_name, arg = argv
    list_states(username, password, db_name, arg)
