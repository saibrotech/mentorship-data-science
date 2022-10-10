from base import Base, engine

# Import the Job table
from tables import Job

# Create the table in the database
if __name__ == "__main__":
    Base.metadata.create_all(engine)