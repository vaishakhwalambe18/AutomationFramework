import pytest


def test_tc1():
    assert True


@pytest.mark.failedones
def test_tc2():
    assert False
