import os
import jwt
import uuid
import hashlib
from urllib.parse import urlencode

import requests
access_key = os.environ['UPBIT_ACCESS_KEY']
secret_key = os.environ['UPBIT_SECRET_KEY']
server_url = "https://api.upbit.com/"

def buy(currency,volume,price):
    #사기
    query = {
        'market': 'KRW-'+currency,
        'side': 'bid',
        'volume': str(volume),
        'price': str(price),
        'ord_type': 'limit',
    }
    post_data(query)

def sell(currency,volume,price):
    #팔기
    query = {
        'market': 'KRW-'+currency,
        'side': 'ask',
        'volume': str(volume),
        'price': str(price),
        'ord_type': 'limit',
    }
    post_data(query)

def post_data(query):
    query_string = urlencode(query).encode()

    m = hashlib.sha512()
    m.update(query_string)
    query_hash = m.hexdigest()

    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
        'query_hash': query_hash,
        'query_hash_alg': 'SHA512',
    }
    jwt_token = jwt.encode(payload, secret_key)
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {"Authorization": authorize_token}

    res = requests.post(server_url + "/v1/orders", params=query, headers=headers)
    return res

if __name__ == '__main__':
    print(sell("ETH", '0.01', '5000'))
    pass
    