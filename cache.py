from pymemcache.client import base

import ast
from request import parse_data
from  datetime import date, datetime, timedelta




client = base.Client(('localhost', 11211))

def cached_data():
    time_today = date.today().strftime('%d.%m.%Y')
    time_yesterday = datetime.strftime(datetime.now() - timedelta(1), '%d.%m.%Y')
    url_today = f"https://www.cbar.az/currencies/{time_today}.xml"
    url_yesterday = f"https://www.cbar.az/currencies/{time_yesterday}.xml"

    result = client.get('data')

    if result:
        last_result = ast.literal_eval(result.decode('utf-8'))
        return last_result
    else:
        try:
            data = (parse_data(url_today))

        except:
            data = (parse_data(url_yesterday))

        client.set('data', data, 5)

        return data


def cache_code(code):
    time_today = date.today().strftime('%d.%m.%Y')
    time_yesterday = datetime.strftime(datetime.now() - timedelta(1), '%d.%m.%Y')
    url_today = f"https://www.cbar.az/currencies/{time_today}.xml"
    url_yesterday = f"https://www.cbar.az/currencies/{time_yesterday}.xml"

    result = client.get(f'{code}')

    if result:
        last_result = ast.literal_eval(result.decode('utf-8'))
        return last_result
    else:
        try:
            data = (parse_data(url_today))
            code_data = list(filter(lambda x: x["code"] == code, data))
        except:
            data = (parse_data(url_yesterday))
            code_data = list(filter(lambda x: x["code"] == code, data))

        client.set(f'{code}', code_data, 5)

        return code_data


# print(cached_data())
# print(cache_code('USD'))
