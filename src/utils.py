def format_datetime(string):
    """
    Редактирование даты под читаемый формат
    """
    return f"{string[8:10]}.{string[5:7]}.{string[:4]} {string[11:16]}"


def get_amount(dict_):
    """
    Редактирование суммы под читаемый формат
    """
    return f"{dict_['amount']} {dict_['currency']['name']}"


def security(card_number):
    """
    Частично скрывает номера карт и счетов
    """
    _ = card_number.split()
    number = _.pop()
    card = " ".join(_)

    if len(number) == 20:
        return f"{card} **{number[-4:]}"
    else:
        return f"{card} {number[:4]} {number[4:6]}** **** {number[-4:]}"


def output(row):
    """
    Вывод операции в читаемом формате
    """
    return f"""{format_datetime(row['date'])} {row['description']}
{security(row['from']) + ' -> ' if 'from' in row.keys() else ''}{security(row['to'])}
{get_amount(row['operationAmount'])}"""
