import pytest


@pytest.fixture
def setup():
    print("Setup Done")


def test_case1(setup):
    print("Test Case 1 Executed")


def test_case2(setup):
    print("Test Case 2 Executed")
