import pytest


@pytest.fixture(scope='module')
def init_driver():
    print('\n========================Class Level  :  SET UP===========================')

    yield
    print('\n=======================Class Level : Tear Down =============================')


def setup_module_level(module):
    print('\n==============MODULE : SET UP===============')


def teardown_module_level(module):
    print('\n============================ TEAR DOWN : MODULE ==================')


def test_m2t1(init_driver):
    a = 2
    b = 2
    print(a, b)
    assert a == b


def test_m2t2():
    print("\nt2m2")
    assert True
