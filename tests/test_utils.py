from src.utils import format_datetime, get_amount, security, output


def test_format_datetime():
    assert format_datetime("2018-04-14T19:35:28.978265") == "14.04.2018 19:35"
    assert format_datetime("2019-09-11T17:30:34.445824") == "11.09.2019 17:30"


def test_get_amount():
    test_dict = {
      "amount": "54280.01",
      "currency": {
        "name": "USD",
        "code": "USD"
      }}
    assert get_amount(test_dict) == "54280.01 USD"


def test_security():
    assert security("Счет 96008924215040031147") == "Счет **1147"
    assert security("Visa Classic 4195191172583802") == "Visa Classic 4195 19** **** 3802"
    assert security("Maestro 3364923093037194") == "Maestro 3364 92** **** 7194"


def test_output():
    test_row = {
    "id": 476991061,
    "state": "CANCELED",
    "date": "2018-11-23T17:47:33.127140",
    "operationAmount": {
      "amount": "26971.25",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод с карты на карту",
    "from": "Visa Gold 7305799447374042",
    "to": "Maestro 3364923093037194"
  }
    res_row = """23.11.2018 17:47 Перевод с карты на карту
Visa Gold 7305 79** **** 4042 -> Maestro 3364 92** **** 7194
26971.25 руб."""
    assert output(test_row) == res_row
