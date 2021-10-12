import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from fishbowl.settings import username, password, host, port, schema_name


database_url = "mysql+pymysql://{}:{}@{}:{}/{}".format(username, password, host, port, schema_name)

engine = create_engine(database_url)
Session = sessionmaker(bind=engine) # type: sqlalchemy.orm.session.sessionmaker
session = Session() # type: sqlalchemy.orm.session.Session
Base = declarative_base(bind=engine) # type: sqlalchemy.ext.declarative.api.DeclarativeMeta

from fishbowl.database.models import *