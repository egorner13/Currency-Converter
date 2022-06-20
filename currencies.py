import requests

currency_list = []
url = 'https://api.coingecko.com/api/v3/exchange_rates'
resp = requests.get(url)
data = resp.json()
each = data['rates']


def curr_list():
    for currency in each.items():
        currency_list.append((currency[1])['name'])
    return currency_list


def value(curr):
    for currency in each.items():
        if ((currency[1])['name']) == curr:
            curr_value = ((currency[1])['value'])
            return curr_value
