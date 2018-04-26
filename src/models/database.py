from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import force_auto_coercion

# TODO set environment variable and vary engine according to env.var
engine = create_engine(
    'sqlite:///',
    echo=True
)
Base = declarative_base()
force_auto_coercion()
Session = sessionmaker(bind=engine, autoflush=True)
