from src.funcs import rm_broken_data, filter_by_state, sort_by_date, get_number_operation


def test_rm_broken_data():
    test_list = ["abcdefg", "abcdef", "", "abcdefg", "0", "abcdefg", "abcdef", "abcde"]
    assert len(rm_broken_data(test_list)) == 5


def test_filter_by_state():
    test_list = [{"id": 1, "state": "EXECUTED"},
                 {"id": 2, "state": "CANCELED"},
                 {"id": 3, "state": "EXECUTED"},
                 {"id": 4, "state": "CANCELED"},
                 {"id": 5, "state": "EXECUTED"}]
    assert len(list(filter_by_state(test_list))) == 3
    assert len(list(filter_by_state(test_list, key="CANCELED"))) == 2
    assert len(list(filter_by_state(test_list, key="EXECUTED"))) == 3


def test_sort_by_date():
    test_list = [{"id": 1, "date": "2018-09-12T21:27:25.241689"},
                 {"id": 2, "date": "2018-10-14T08:21:33.419441"},
                 {"id": 3, "date": "2018-01-26T15:40:13.413061"},
                 {"id": 4, "date": "2018-11-29T07:18:23.941293"},
                 {"id": 5, "date": "2018-04-14T19:35:28.978265"}]
    res = [{'id': 4, 'date': '2018-11-29T07:18:23.941293'},
           {'id': 2, 'date': '2018-10-14T08:21:33.419441'},
           {'id': 1, 'date': '2018-09-12T21:27:25.241689'},
           {'id': 5, 'date': '2018-04-14T19:35:28.978265'},
           {'id': 3, 'date': '2018-01-26T15:40:13.413061'}]

    assert sort_by_date(test_list) == res


def test_get_number_operation():
    test_list = range(20)
    assert len(get_number_operation(test_list)) == 5
    assert len(get_number_operation(test_list, 3)) == 3
    assert len(get_number_operation(test_list, 7)) == 7
    assert len(get_number_operation(test_list, 10)) == 10
