#! /home/dimapb/.cache/pypoetry/virtualenvs/src-PhVsYnOQ-py3.10/bin/python

import json


def get_json(file_name):
    """
    Чтение json
    """
    with open(file_name, "r", encoding="utf-8") as file:
        return json.load(file)


def rm_broken_data(data):
    """
    Удвляем сломанные данные
    """
    return [row for row in data if len(row) > 5]
    

def filter_by_state(data, key="EXECUTED"):
    """
    Фильтр выполненых операций
    """
    return filter(lambda x: x["state"] == key, data)


def sort_by_date(data, parametr="date", direction=True):
    """
    Упорядочивает операции по дате, в теории можно добавить настрйку по сумме перевода
    """
    return sorted(data, key=lambda x: x[parametr], reverse=direction)
    

def get_number_operation(data, count=5):
    """
    Выдает количество операций
    """
    return data[:count]
