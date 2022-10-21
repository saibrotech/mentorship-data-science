import json
import os
from sqlalchemy import *
from sqlalchemy.orm import declarative_base, mapper, Session
from sqlalchemy.schema import MetaData

BASE_PATH = os.path.abspath(__file__ + '/../')
DATA_PATH = f'{BASE_PATH}/data/'
JSON_PATH = DATA_PATH + 'json/'

def setup_database():
    """
    Connect to PostgreSQL database and create tables
    """
    engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/postgres')
    session = Session(engine)
    Base = declarative_base()
    class Job(Base):
        __tablename__ = "job"

        id = Column(Integer, primary_key=True)
        title = Column(String(255))
        date_posted = Column(Date)
        experience_level = Column(String(55))
        type = Column(String(55))
        location = Column(String(55))
        requirements = Column(String(255))
        link = Column(String(255))
        category = Column(String(55))
        company = Column(String(55))
    Job.__table__.create(bind=engine, checkfirst=True)
    print('Table created successfuly!')
    

def read_json():
    """
    Read JSON files using json library
    """
    json_list = os.listdir(JSON_PATH)
    for json_file in json_list:
        id, extension = os.path.splitext(json_file)
        json_file
        
        print(f'Loading', json_file)
        data = json.load(open(f'{JSON_PATH}{json_file}'))
        map_data(data)

def map_data(data):
    """
    Make an association between database table and json data structure
    """
    metadata = MetaData()
    
    columns = (
        Column('id', Integer, primary_key=True),
        Column('title', String(100)),
        Column('date', Date),
        Column('level', String(20)),
        Column('type', String(10)),
        Column('location', String(100)),
        Column('description', String(300)),
        Column('link', String(200)),
        Column('company', String(100)),
        Column('category', String(3)),
    )
    
    jobs = Table('jobs', metadata, *columns)    
    
    class Jobs(object):
        def __init__(self, json_file):
            for key, value in data.iteritems():
                setattr(self, key, value)
    
    mapper(Jobs, jobs)
    print(f'Job entry mapped successfuly')

def insert_new_jobs():
    """
    Insert new jobs to database
    """


def delete_old_jobs():
    """
    Delete jobs that are no longer available
    """
   

# Main function called inside the execute.py script
def main():
    print("[Load] Start")
    print("[Load] Inserting new rows")
    setup_database()
    read_json()
    print("[Load] End")