#!/usr/bin/python3
"""
Lists all State objects that contain the letter
    a from the database hbtn_0e_6_usa
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
    # Extract all State that contain the letter a
    rows = session.query(State).filter(State.name.like('%a%')).\
        order_by(State.id).all()
    # Print results
    for state in rows:
        print(f"{state.id}: {state.name}")
    session.close()  # Close session
