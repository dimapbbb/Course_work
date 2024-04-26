#! /home/dimapb/.cache/pypoetry/virtualenvs/src-PhVsYnOQ-py3.10/bin/python

from funcs import get_data, Operation


def main():
    operations = get_data("operations.json")

    for row in operations:
        operation = Operation(row)
        print(operation)
        print()


main()



