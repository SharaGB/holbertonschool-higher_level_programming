#!/usr/bin/python3
"""
Prints the State object with the name passed as argument
    from the database hbtn_0e_6_usa
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
    # Extract all name passed as argument
    row = session.query(State).filter(State.name == sys.argv[4]).all()
    # Print results
    if row:
        for states in row:
            print(f"{states.id}")
    else:
        print("Not found")  # If no state has the name you searched
    session.close()  # Close session
