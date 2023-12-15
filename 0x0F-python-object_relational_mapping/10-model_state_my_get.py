#!/usr/bin/python3
"""Module documentation"""
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_count = session.query(State).\
        filter(State.name.like(sys.argv[4])).order_by(State.id).count()
    if (state_count == 0):
        print('Not found')
    else:
        print(state_count)
