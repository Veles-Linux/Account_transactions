from utils import date_operations_format


def test_date_operations_format():
    assert date_operations_format('1954-12-01T23:06:44') == '01.12.1954'
