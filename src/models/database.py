import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import force_auto_coercion

MYSQL_USERNAME = os.environ['MYSQL_USERNAME']
MYSQL_PASSWORD = os.environ['MYSQL_PASSWORD']
MYSQL_HOST = os.environ['MYSQL_HOST']

db_url = 'mysql+pymysql://{}:{}@{}/conduit_db'\
    .format(MYSQL_USERNAME, MYSQL_PASSWORD, MYSQL_HOST)
engine = create_engine(db_url, echo=True)
Base = declarative_base()
force_auto_coercion()
Session = sessionmaker(bind=engine, autoflush=True)
