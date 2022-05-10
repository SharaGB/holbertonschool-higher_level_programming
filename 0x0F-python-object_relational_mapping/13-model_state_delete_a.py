#!/usr/bin/python3
"""
Deletes all State objects with a name containing the
    letter 'a' from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create an engine
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}\
        @localhost/{sys.argv[3]}', pool_pre_ping=True)
    # Create a metadata instance (Table)
    Base.metadata.create_all(engine)
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    session = Session()  # Create a new session
    # Deletes all State objects with a name containing the letter 'a'
    state = session.query(State).filter(State.name.like('%a%')).all()
    for letter in state:
        session.delete(letter)
    # Issue all remaining changes to the database and commit the transaction
    session.commit()
    session.close()  # Close session
