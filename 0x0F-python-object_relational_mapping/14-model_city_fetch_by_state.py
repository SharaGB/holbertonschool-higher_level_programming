#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa
"""
import sys
from model_city import City
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
    obj = session.query(State, City).filter(State.id == City.state_id)\
        .order_by(City.id)
    for states, cities in obj:
        print(f"{states.name}: ({cities.id}) {cities.name}")
    session.close()  # Close session
