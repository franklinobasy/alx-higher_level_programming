#!/usr/bin/python3
'''
a script that lists all State objects that contain
the letter a from the database hbtn_0e_6_usa.
'''

import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    url = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(
        url.format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    data = session.query(State).order_by(State.id)\
                               .filter(State.name.like("%a%")).all()
    for row in data:
        print("{}: {}".format(row.id, row.name))
    session.close()
