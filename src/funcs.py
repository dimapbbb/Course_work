#! /home/dimapb/.cache/pypoetry/virtualenvs/src-PhVsYnOQ-py3.10/bin/python

import json


def get_data(file_name, count_operations=5):
    """
    getting the last 5 operation from json file, quantity can be customized
    """
    with open(file_name, "r", encoding="utf-8") as file:          # read file json
        data = json.load(file)

    data = [row for row in data if len(row) > 5]                  # removing broken data
    data = filter(lambda x: x["state"] == "EXECUTED", data)       # filter by key EXECUTED
    data = sorted(data, key=lambda x: x["date"], reverse=True)    # sort by date
    
    return data[:count_operations]


class Operation():
    def __init__(self, operation):
        self.operation = operation
        self.date = operation["date"]
        self.description = operation["description"]
        self.to = operation["to"]
        self.amount = operation["operationAmount"]["amount"] + " " + operation["operationAmount"]["currency"]["name"]
        
    def __str__(self):
        return f"""
                {self.reformat_date()} {self.description}
                {self.receiving_sender()}{self.to}
                {self.amount}  
                """

    def reformat_date(self):
        return f"{self.date[8:10]}.{self.date[5:7]}.{self.date[:4]}"

    def receiving_sender(self):
        if "from" in self.operation.keys():
            return f"{self.operation['from']} -> "
        else:
            return ""
