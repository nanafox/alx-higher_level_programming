#!/usr/bin/python3

"""This script updates the name of State object with `id` number 2 to
'New Mexico' in the `hbtn_0e_6_usa` database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def update_state(
    username: str, password: str, database: str, state_id: int, new_name: str
) -> None:
    """Lists the State objects that contains the letter `a` in a database.

    Args:
        username (str): The username for the connection.
        password (str): The password of the user.
        database (str): The database to connect to.
        state_id (int): The id of the state to update.
        new_name (str): The name to update old name to.
    """
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"
    )

    Base.metadata.create_all(engine)

    with Session(engine) as session:
        query = session.query(State).filter(State.id == state_id)
        query.update({State.name: new_name})

        session.commit()


if __name__ == "__main__":
    try:
        update_state(sys.argv[1], sys.argv[2], sys.argv[3], 2, "New Mexico")
    except IndexError:
        sys.stderr.write(
            f"Usage: {sys.argv[0]} <username> <password> <db_name>\n"
        )
        sys.exit(1)
