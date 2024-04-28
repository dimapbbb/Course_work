#! /home/dimapb/.cache/pypoetry/virtualenvs/src-PhVsYnOQ-py3.10/bin/python
from os.path import abspath
from funcs import get_json, rm_broken_data, filter_by_state, sort_by_date, get_number_operation  
from utils import format_datetime, get_amount, security


def main():
    data = get_json(abspath("./src/operations.json"))

    data = rm_broken_data(data)

    data = filter_by_state(data)
    
    data = sort_by_date(data)

    data = get_number_operation(data)
    
    for row in data:
        print(
f"""{format_datetime(row['date'])} {row['description']}
{security(row['from']) + ' -> ' if 'from' in row.keys() else ''}{security(row['to'])}
{get_amount(row['operationAmount'])}"""
             )
        print()

main()
