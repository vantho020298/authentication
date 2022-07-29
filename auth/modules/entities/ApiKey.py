from config import db, base
from sqlalchemy import Column, String  


class ApiKey(base):
    __tablename__ = 'api_key'
    key = Column(String(100), primary_key = True)
    value = Column(String(100), nullable=False)
    description = Column(String(200)) 

    def __init__(self, key, value, description = None):
        self.key = key
        self.value = value
        self.description = description

    def __repr__(self):
        return '<id {}>'.format(self.key)


base.metadata.create_all(db)