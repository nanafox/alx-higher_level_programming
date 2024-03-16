#!/usr/bin/python3

"""This module prints State object with the name passed as argument from the
`hbtn_0e_6_usa` database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def get_state_by_name(
    username: str, password: str, database: str, state_name: str
) -> None:
    """Lists the State objects that contains the letter `a` in a database.

    Args:
        username (str): The username for the connection.
        password (str): The password of the user.
        database (str): The database to connect to.
        state_name (str): The name of the state to search.
    """
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"
    )

    Base.metadata.create_all(engine)

    with Session(engine) as session:
        state = session.query(State).filter(State.name == state_name).first()

        if state:
            print(f"{state.id}")
        else:
            print("Not found")


if __name__ == "__main__":
    try:
        get_state_by_name(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    except IndexError:
        sys.stderr.write(
            f"Usage: {sys.argv[0]} <username> <password> "
            "<database> <state name to search>\n"
        )
        sys.exit(1)
