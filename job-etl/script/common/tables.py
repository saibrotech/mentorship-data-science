from sqlalchemy import cast, Column, Integer, String, Date
from sqlalchemy.orm import column_property

from common.base import Base


class JobRawAll(Base):
    __tablename__ = "job_raw_all"

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    date_posted = Column(String(55))
    experience_level = Column(String(55))
    type = Column(String(55))
    location = Column(String(55))
    requirements = Column(String(255))
    link = Column(String(255))
    category = Column(String(55))
    company = Column(String(55))
   
class JobCleanAll(Base):
    __tablename__ = "job_clean_all"

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    date_posted = Column(String(55))
    experience_level = Column(String(55))
    type = Column(String(55))
    location = Column(String(55))
    requirements = Column(String(255))
    link = Column(String(255))
    category = Column(String(55))
    company = Column(String(55))