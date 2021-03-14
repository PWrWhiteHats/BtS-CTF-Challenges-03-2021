import requests
from flask import abort
import time
import logging

logger = logging.getLogger('gunicorn.error')

def get_location_for(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    if response.status_code == 429:
        time.sleep(0.5)
        return 'Try again in a while'
    elif 'fail' in response.text:
        logger.error(f"{response.text}")
        if 'reserved range' in response.text or 'private range' in response.text:
            return "somewhere, I can't really say where..."
        return 'Unknown'
    else:
        time.sleep(0.5)
        json = response.json()
        logger.info(f"Status '{json.get('status')}' for IP '{json.get('query')}'")
        return f"{json.get('country')} {json.get('regionName')} {json.get('city')}"

