#! /home/dimapb/.cache/pypoetry/virtualenvs/src-PhVsYnOQ-py3.10/bin/python

import json


def get_data(file_name):
    """
    getting the last 5 operation from json file
    """
    with open(file_name, "r", encoding="utf-8") as file:          # read file json
        data = json.load(file)

    data = [row for row in data if len(row) > 5]             # removing broken data
    data = filter(lambda x: x["state"] == "EXECUTED", data)       # filter by key EXECUTED
    data = sorted(data, key=lambda x: x["date"], reverse=True)    # sort by date
    
    return data[:5]
