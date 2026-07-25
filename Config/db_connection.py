from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

""" Load and Get Envs """

# Load Envs
load_dotenv()

# Get Route to Databse
DB_URL = os.getenv("DATABASE_URL")


""" Creation the sessions engine """

# creation the Engine
engine = create_engine(
    DB_URL,
    pool_pre_ping = True,
    pool_recycle = 3600
)

# Create the session factory
SessionLocal = sessionmaker(
    autocommit = False, 
    autoflush = False, 
    bind = engine
)


""" Creation to the Base Class for Databse Models """

# Base Class for DB Models
Base = declarative_base()