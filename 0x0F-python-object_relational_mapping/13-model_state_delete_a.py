#!/usr/bin/python3

"""This script deletes State objects with a name containing the letter `a`
from the `hbtn_0e_6_usa` database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    try:
        username, password, database = sys.argv[1:]
    except IndexError:
        sys.stderr.write(
            f"Usage: {sys.argv[0]} <username> <password> <db_name>\n"
        )
        sys.exit(1)

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"
    )

    Base.metadata.create_all(engine)

    with Session(engine) as session:
        query = session.query(State).filter(State.name.like("%a%"))
        query.delete()

        session.commit()
