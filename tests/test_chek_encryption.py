from utils import chek_encryption


def test_chek_encryption():
    assert chek_encryption('12341234123412341234') == '**1234'
