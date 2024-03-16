#!/usr/bin/python3

"""This module prints all City objects from the `hbtn_0e_14_usa` database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import State, Base
from model_city import City


if __name__ == "__main__":
    try:
        username, password, database = sys.argv[1:]
    except IndexError:
        sys.stderr.write(
            f"Usage: {sys.argv[0]} <username> <password> <database\n"
        )
        sys.exit(1)

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"
    )

    Base.metadata.create_all(engine)

    with Session(engine) as session:
        city_by_state = (
            session.query(State.name, City.id, City.name)
            .order_by(City.id)
            .join(City)
            .filter(State.id == City.state_id)
            .all()
        )

        for city in city_by_state:
            print(f"{city[0]}: ({city[1]}) {city[2]}")
