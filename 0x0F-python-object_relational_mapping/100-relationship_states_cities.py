#!/usr/bin/python3

"""This script creates the State object 'California' with the City
'San Francisco' in the database `hbtn_0e_100_usa."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_city import City
from relationship_state import State, Base

if __name__ == "__main__":
    try:
        username, password, database = sys.argv[1:]
    except ValueError:
        sys.stderr.write(
            f"Usage: {sys.argv[0]} <username> <password> <database>\n"
        )
        sys.exit(1)

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}",
        pool_pre_ping=True,
    )

    Base.metadata.create_all(engine)
    with Session(engine) as session:
        state = State(name="California")
        state.cities = [City(name="San Francisco")]
        session.add(state)
        session.commit()
