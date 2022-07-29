from flask import Flask
from sqlalchemy import create_engine  
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker
import os
import redis


POSTGRES_PASSWORD=os.getenv('POSTGRES_PASSWORD')
POSTGRES_USER=os.getenv('POSTGRES_USER')
POSTGRES_DB=os.getenv('POSTGRES_DB')
POSTGRES_PORT=os.getenv('POSTGRES_PORT')
POSTGRES_HOST=os.getenv('POSTGRES_HOST')
CACHE_PASSWORD=os.getenv('CACHE_PASSWORD')
CACHE_PORT=os.getenv('CACHE_PORT')
CACHE_HOST=os.getenv('CACHE_HOST')

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db_string = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_PORT, POSTGRES_DB)
db = create_engine(db_string)  
base = declarative_base()

Session = sessionmaker(db)
session = Session()

cache = redis.Redis(
    host=CACHE_HOST,
    port=CACHE_PORT, 
    password=CACHE_PASSWORD)