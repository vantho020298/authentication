import csv
from config import cache
import os
import json
from modules.aesutils import decrypt, encrypt
from datetime import datetime

TOKEN_EXPIRE_TIME=os.getenv('TOKEN_EXPIRE_TIME')
SECRET_KEY=os.getenv('SECRET_KEY')


def is_trusted(headers, apiKeys):
    for apiKey in apiKeys:
        raw_header, header_value, timestamp = get_item(headers, apiKey.key)
        if is_expired(timestamp):
            return False

        if is_token_exists(raw_header):
            return False

        if header_value != decrypt(SECRET_KEY, apiKey.value):
            return False
            
        cache.setex(raw_header, int(TOKEN_EXPIRE_TIME), "1")

    return True


def is_token_exists(token):
    if cache.exists(token) == 1:
        return True
    return False


def is_expired(timestamp):
    dt = datetime.now()
    current_timestamp = datetime.timestamp(dt)

    return current_timestamp - timestamp / 1000 > int(TOKEN_EXPIRE_TIME)



def get_item(obj, item_name):
    if item_name in obj:
        data = decrypt(SECRET_KEY, obj[item_name])
        data_json = json.loads(data)
        return obj[item_name], data_json['value'], data_json['timestamp']
    
    return None, None