import requests, json

def get_price(currency):
    url = "https://api.upbit.com/v1/orderbook/"

    querystring = {"markets":"KRW-"+currency}

    headers = {"Accept": "application/json"}

    response = requests.request("GET", url, headers=headers , params=querystring)

    return json.loads(response.text)[0]['orderbook_units'][0]


if __name__ == "__main__":
    print( get_price("ETH") )