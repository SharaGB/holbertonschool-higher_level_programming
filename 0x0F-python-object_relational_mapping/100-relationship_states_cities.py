#!/usr/bin/python3
"""
Creates the State “California” with the City “San Francisco”
"""
import sys
from relationship_city import City
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

    newState = State(name='California')
    newState.cities = [City(name='San Francisco')]
    session.add(newState)
    # Issue all remaining changes to the database and commit the transaction
    session.commit()
    session.close()  # Close session
