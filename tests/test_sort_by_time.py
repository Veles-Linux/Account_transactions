from utils import sort_by_time


def test_sort_by_time():
    assert sort_by_time()[0] > sort_by_time()[1]
    assert sort_by_time()[3] > sort_by_time()[6]
    assert sort_by_time()[3] == sort_by_time()[3]
    assert sort_by_time()[-1] < sort_by_time()[-4]

