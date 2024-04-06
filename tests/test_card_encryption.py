from utils import card_encryption


def test_card_encryption():
    assert card_encryption('1234123412341234') == '1234 12** **** 1234'
    assert card_encryption('12341234123412341234') == '12341 2**** ***** *1234'
