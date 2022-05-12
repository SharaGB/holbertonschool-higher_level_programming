#!/usr/bin/python3
"""
Lists all State objects, and corresponding City objects,
    contained in the database hbtn_0e_101_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State

if __name__ == "__main__":
    # Create an engine
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}\
        @localhost/{sys.argv[3]}', pool_pre_ping=True)
    # Create a metadata instance (Table)
    Base.metadata.create_all(engine)
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    session = Session()  # Create a new session
    obj = session.query(State).all()
    for state in obj:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")
    session.close()  # Close session
