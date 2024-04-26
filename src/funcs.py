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
                {self.receiving_sender()}{self.receiving_recipient()}
                {self.amount}  
                """

    def reformat_date(self):
        """
        date to readble format
        """
        return f"{self.date[8:10]}.{self.date[5:7]}.{self.date[:4]}"

    def get_number(self, string):
        """
        getting the card name and number
        """
        _ = string.split()
        number = _.pop()
        name = " ".join(_)
        return name, number

    def receiving_sender(self):
        """
        receiving the sender if any
        """
        if "from" in self.operation.keys():
            name, number = self.get_number(self.operation['from'])
            return f"{name} {self.security(number)} -> "
        else:
            return ""

    def receiving_recipient(self):
        """
        receiving the recepient
        """
        name, number = self.get_number(self.to)
        return f"{name} {self.security(number)}"

    def security(self, number):
        """
        hiding account numbers
        """
        if len(number) == 20:
            return f"**{number[-4:]}"
        else:
            return f"{number[:4]} {number[4:6]}** **** {number[-4:]}" 
        
