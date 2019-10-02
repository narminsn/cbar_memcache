from pymemcache.client import base
import ast
from request import parse_data
from  datetime import date, datetime, timedelta


time_today = date.today().strftime('%d.%m.%Y')

time_yesterday = datetime.strftime(datetime.now() - timedelta(1), '%d.%m.%Y')

url_today = f"https://www.cbar.az/currencies/{time_today}.xml"
url_yesterday = f"https://www.cbar.az/currencies/{time_yesterday}.xml"

client = base.Client(('localhost', 11211))

def cached_data():
    result = client.get('city')
    # print(result)
    if result:
        last_result = ast.literal_eval(result.decode('utf-8'))
        return last_result
    else:
        try:
            data = (parse_data(url_today))
            client.set('data', data, 8)
            result = client.get('data')
            last_result = ast.literal_eval(result.decode('utf-8'))
            return last_result

        except:
            data = (parse_data(url_yesterday))
            client.set('data', data, 8)
            result = client.get('data')
            last_result = ast.literal_eval(result.decode('utf-8'))
            return last_result


# print(cached_data())