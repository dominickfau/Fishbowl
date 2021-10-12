import sqlalchemy
import logging
import os
import sys
from logging.config import dictConfig
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


from fishbowl.settings import username, password, host, port, schema_name
database_url = "mysql+pymysql://{}:{}@{}:{}/{}".format(username, password, host, port, schema_name)

# Find the current users home directory
home_dir = os.path.expanduser("~")
documents_dir = os.path.join(home_dir, "Documents")
program_dir = os.path.join(documents_dir, "Fishbowl_MySQL")
logs_dir = os.path.join(program_dir, "Logs")

if not os.path.exists(program_dir):
    os.mkdir(program_dir)

if not os.path.exists(logs_dir):
    os.mkdir(logs_dir)


dictConfig({
    "version": 1,
    "formatters": {
        "default": {
            "datefmt": "%Y-%m-%d %H:%M:%S",
            "format": "%(asctime)s [%(levelname)s] in %(name)s.%(module)s: %(message)s",
        }
    },
    "handlers": {
        "main": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(logs_dir, "main.log"),
            "maxBytes": 10 * 1024 * 1024,
            "backupCount": 3,
            "formatter": "default"
        },
        "sql_pool": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(logs_dir, "sql_pool.log"),
            "maxBytes": 10 * 1024 * 1024,
            "backupCount": 3,
            "formatter": "default"
        },
        "sql_engine": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(logs_dir, "sql_engine.log"),
            "maxBytes": 10 * 1024 * 1024,
            "backupCount": 3,
            "formatter": "default"
        },
        "exception_log": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(logs_dir, "exception_log.log"),
            "maxBytes": 10 * 1024 * 1024,
            "backupCount": 3,
            "formatter": "default"
        }
    },
    "loggers": {
        "root": {
            "level": "INFO",
            "handlers": ["main", "sql_pool", "sql_engine", "exception_log"]
        },
        "sqlalchemy.engine": {
            "level": "INFO",
            "handlers": ["sql_engine"]
        },
        "sqlalchemy.pool": {
            "level": "INFO",
            "handlers": ["sql_pool"]
        },
        "exception_log": {
            "level": "INFO",
            "handlers": ["exception_log"]
        }
    }
})

logger = logging.getLogger("root")
logger.info("=" * 60)
logger.info("Starting...")

def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    
    print("Uncaught exception:", exc_type, exc_value)
    logger.critical(f"Uncaught exception: {exc_type, exc_value}")
    logging.getLogger("exception_log").error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))
    

sys.excepthook = handle_exception

engine = create_engine(database_url)
Session = sessionmaker(bind=engine) # type: sqlalchemy.orm.session.sessionmaker
session = Session() # type: sqlalchemy.orm.session.Session
Base = declarative_base(bind=engine)

from fishbowl.database.models import *