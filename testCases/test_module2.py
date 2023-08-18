import pytest


def test_m2t1():
    a = 1
    b = 2
    assert a == b


@pytest.mark.failedones
def test_m2t2():
    assert True
