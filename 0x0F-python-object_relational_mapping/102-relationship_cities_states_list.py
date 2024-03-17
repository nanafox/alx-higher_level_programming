#!/usr/bin/python3

"""This script lists all City objects from the database hbtn_0e_101_usa"""

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
        query = session.query(State).order_by(State.id)
        for state in query:
            for city in state.cities:
                print(f"{city.id}: {city.name} -> {state.name}")
