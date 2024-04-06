from utils import name_card


def test_name_card():
    assert name_card('Visa 1234123412341234') == 'Visa'
    assert name_card('Счет 12341234123412341234') == 'Счет'
