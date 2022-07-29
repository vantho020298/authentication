from config import session
from modules.entities.ApiKey import ApiKey
from modules.aesutils import decrypt, encrypt
import os
SECRET_KEY=os.getenv('SECRET_KEY')


def add_or_update(data):
    apiKeys = session.query(ApiKey)
    for attr, value in data.items():
        try:
            apiKey = apiKeys.filter(ApiKey.key==attr).one()
            apiKey.value = encrypt(SECRET_KEY, value)
        except:
            session.add(ApiKey(attr, encrypt(SECRET_KEY, value)))
    session.commit()


def delete(data):
    apiKeys = session.query(ApiKey)
    for attr, value in data.items():
        try:
            apiKeys.filter(ApiKey.key==attr).delete()
        except:
            pass
    session.commit()
