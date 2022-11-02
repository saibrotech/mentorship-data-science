import json
import os
from sqlalchemy import create_engine, Column, String, exists, Date, insert
from sqlalchemy.orm import declarative_base, Session
import datetime as dt

BASE_PATH = os.path.abspath(__file__ + '/../')
DATA_PATH = f'{BASE_PATH}/data/'
JSON_PATH = DATA_PATH + 'json/'

engine = create_engine(
    'postgresql+psycopg2://postgres:postgres@localhost:5432/postgres')
session = Session(engine)
Base = declarative_base()


def read_json():
    """
    Read JSON files using json library
    """
    json_list = os.listdir(JSON_PATH)
    for json_file in json_list:
        id, extension = os.path.splitext(json_file)
        json_file
        print(f'Loading', json_file)
        json_data = json.load(open(f'{JSON_PATH}{json_file}'))
        insert_data(json_data)

    session.commit()


class Job(Base):

    def __init__(self, json_data):
        print(type(json_data), json_data.items)
        for key, value in json_data.items():
            setattr(self, key, value)

    __tablename__ = "job"

    id = Column(String(), primary_key=True, nullable=False)
    title = Column(String())
    date = Column(Date())
    level = Column(String())
    type = Column(String())
    location = Column(String())
    description = Column(String())
    link = Column(String())
    category = Column(String())
    company = Column(String())
    e_date = Column(Date())
    t_date = Column(Date())
    l_date = Column(Date(), default=dt.datetime.today().strftime('%d/%m/%Y'))


def setup_database():
    """
    Connect to PostgreSQL database and create tables
    """
    Job.__table__.create(bind=engine, checkfirst=True)
    print('Table created successfuly!')


def insert_data(json_data):
    """
    Insert operation: add new data
    """

    existing = session.query(exists().where(Job.id == json_data['id'])).scalar()

    if not existing:
        job_row = Job(json_data)
        session.add(job_row)    

    
# Main function called inside the execute.py script
def main():
    print("[Load] Start")
    print("#[Load] Inserting new rows")
    setup_database()
    read_json()
    print("[Load] End")

if __name__ == "__main__":
    main()