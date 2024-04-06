from utils import sort_by_operations


def test_sort_by_operations():
    assert sort_by_operations()[0]['date'] > sort_by_operations()[1]['date']
    assert sort_by_operations()[3]['date'] > sort_by_operations()[5]['date']
    assert sort_by_operations()[-3]['date'] > sort_by_operations()[-1]['date']
    assert sort_by_operations()[2]['date'] == sort_by_operations()[2]['date']
