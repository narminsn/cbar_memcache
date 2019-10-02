import requests
import datetime
import requests
import json, xmljson
from lxml.html import fromstring, tostring



symvol_list = (
("ə", "e"), ("ü", "u"), ("ç", "c"), ("ı", "i"), ("ö", "o"), ("ğ", "g"), ('ş', 's'), ("İ", "I"), ('Ğ', 'G'), ('Ü', 'U'),
('Ö', 'O'),('Ə', 'E'),('Ş', 'S'),('Ç', 'C'))


def replace_func(word):
    for before, after in symvol_list:
        if before in word:
            word = word.replace(before, after)
    return word

def parse_data(url):
    second = datetime.datetime.now().second
    response = requests.get(url)

    bank_mezenne = []
    xml = fromstring(response.content)
    json_data = json.dumps(xmljson.badgerfish.data(xml))

    data = json.loads(json_data)
    # list_data1 = data["valcurs"]["valtype"][0]
    list_data2 = data["valcurs"]["valtype"][1]
    for item in list_data2["valute"]:
        code = replace_func(item["@code"])
        name = replace_func(item["name"]["$"])


        obj = {
            "code": code,
            "name": name,
            "value": item["value"]["$"],
            'time': second
        }

        bank_mezenne.append(obj)

    return bank_mezenne
