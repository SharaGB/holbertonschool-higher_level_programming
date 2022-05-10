#!/usr/bin/python3
"""
Adds the State object “Louisiana” to the database hbtn_0e_6_usa
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
    newStates = State(name='Louisiana')
    session.add(newStates)
    # Issue all remaining changes to the database and commit the transaction
    session.commit()
    print(f"{newStates.id}")
    session.close()  # Close session
