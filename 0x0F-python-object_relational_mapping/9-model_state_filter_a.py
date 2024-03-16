#!/usr/bin/python3

"""This module prints State objects that contains the letter `a` from the
`hbtn_0e_6_usa` database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def get_state_with_letter_a(
    username: str, password: str, database: str
) -> None:
    """Lists the State objects that contains the letter `a` in a database.

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
        state_with_a = (
            session.query(State)
            .order_by(State.id)
            .filter(State.name.like("%a%"))
        )

        for state in state_with_a:
            print(f"{state.id}: {state.name}")


if __name__ == "__main__":
    try:
        get_state_with_letter_a(sys.argv[1], sys.argv[2], sys.argv[3])
    except IndexError:
        sys.stderr.write(
            f"Usage: {sys.argv[0]} <username> <password> <db_name>\n"
        )
        sys.exit(1)
