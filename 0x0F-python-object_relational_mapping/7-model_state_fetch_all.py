#!/usr/bin/python3

"""This module prints all the State objects from the
·`hbtn_0e_6_usa` database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def get_all_states(username: str, password: str, database: str) -> None:
    """Lists all State objects in a database

    Args:
        username (str): The username for the connection.
        password (str): The password of the user.
        database (str): The database to connect to.
    """
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"
    )

    Base.metadata.create_all(engine)

    with Session(engine) as session:
        result = session.query(State).order_by(State.id).all()

        for state in result:
            print(f"{state.id}: {state.name}")


if __name__ == "__main__":
    try:
        get_all_states(sys.argv[1], sys.argv[2], sys.argv[3])
    except IndexError:
        sys.stderr.write(
            f"Usage: {sys.argv[0]} <username> <password> <db_name>\n"
        )
        sys.exit(1)
