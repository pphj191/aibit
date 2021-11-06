import requests, json

url = "https://api.upbit.com/v1/market/all"

querystring = {"isDetails":"false"}

headers = {"Accept": "application/json"}

response = requests.request("GET", url, headers=headers, params=querystring)
a=(eval(response.text))
b= json.loads((response.text))

for i in b:
    print(i)

# {'market': 'BTC-OXT', 'korean_name': '오키드', 'english_name': 'Orchid'}
# {'market': 'BTC-PLA', 'korean_name': '플레이댑', 'english_name': 'PlayDapp'}

# print((b))