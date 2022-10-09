#!/usr/bin/python3
"""
A script that deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                    sys.argv[2],
                                                    sys.argv[3])
        )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    data = session.query(State).filter(State.name.like("%a%"))\
                               .delete(synchronize_session='fetch')
    session.commit()
    session.close()
