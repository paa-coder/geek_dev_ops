import requests
import sys
import json

def cretae_question(question,type):
    try:
        string = input(question.strip()+" или введите exit чтобы прервать выполнение скрипта: ")
        if string=="exit":
            sys.exit()
        else:
            return type(string)
    except TypeError as e:
        print("Ошибка: не корректно введено значение")
        return cretae_question(question,type)

def get_sity(question):
    string = cretae_question(question,str)
    try:
        response = requests.get("https://autocomplete.travelpayouts.com/places2",params={"term":string,"locale":"ru","types[]":"city"})
        response.raise_for_status()
    except Exception as err:
        print(f'ошибка в получении данных с сайта www.travelpayouts.com: {err}')
        return get_sity(question)
    else:
        json = response.json()
        if not json:
            print(f'город не найден')
            return get_sity(question)
        elif len(json)>1:
            print(f'найдено несколько городов берем первый')
        return json[0]


def get_price_info(out_json,to_json):

    params={
        'origin': out_json["code"],
        'destination': to_json["code"]
        }
    try:
        response = requests.get("http://min-prices.aviasales.ru/calendar_preload",params=params)
        response.raise_for_status()
    except Exception as err:
        print(f'Oошибка в получении данных с сайта min-prices.aviasales.ru: {err}')  # Python 3.6
    else:
        return response.json()["best_prices"][0]


print(get_price_info(get_sity("укажите город вылета"),get_sity("укажите город прибыти")))
