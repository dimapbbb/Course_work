#! /home/dimapb/.cache/pypoetry/virtualenvs/src-PhVsYnOQ-py3.10/bin/python
from os.path import dirname, join
from funcs import get_json, rm_broken_data, filter_by_state, sort_by_date, get_number_operation  
from utils import output


def main():
    current_dir = dirname(__file__)
    operations_path = join(current_dir, "operations.json")

    all_operations = get_json(operations_path)

    valid_operations = rm_broken_data(all_operations)

    filtred_operations = filter_by_state(valid_operations)
    
    sorted_operations = sort_by_date(filtred_operations)

    outputable_operations = get_number_operation(sorted_operations)
    
    for operation in outputable_operations:
        print(output(operation))
        print()

main()
