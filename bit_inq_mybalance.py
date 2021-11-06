import os
import jwt
import uuid
import hashlib
from urllib.parse import urlencode

import requests

def get_balance(using_market):        
    access_key = os.environ['UPBIT_ACCESS_KEY']
    secret_key = os.environ["UPBIT_SECRET_KEY"]
    server_url = "https://api.upbit.com/"

    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
    }

    jwt_token = jwt.encode(payload, secret_key)
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {"Authorization": authorize_token}

    res = requests.get(server_url + "/v1/accounts", headers=headers)

    print((res.json()[1]))
    # {'currency': 'ETH', 'balance': '0.02706605', 'locked': '0.0', 'avg_buy_price': '3813018.0106', 'avg_buy_price_modified': False, 'unit_currency': 'KRW'}
    
    # using_market의 순서대로 balance를 줘야함.
    coins_now = []
    for currency in using_market:
        for dic_currency in res.json():
            if dic_currency['currency'] == currency :
                coins_now.append(dic_currency)

    return coins_now

if __name__ == "__main__" :
    print(get_balance("ETH"))