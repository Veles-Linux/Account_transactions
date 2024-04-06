from utils import extend_operations


def test_extend_operations():
    for i in extend_operations():
        assert i['state'] == 'EXECUTED'
