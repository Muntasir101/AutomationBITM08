import pytest


@pytest.mark.order(4)
def test_demo1_methodA(oneTimeSetUp, setUp):
    print("Running conftest demo1 method A")


@pytest.mark.order(1)
def test_demo1_methodB(oneTimeSetUp, setUp):
    print("Running conftest demo1 method B")


@pytest.mark.order(3)
def test_demo1_methodC(oneTimeSetUp, setUp):
    print("Running conftest demo1 method C")


@pytest.mark.order(2)
def test_demo1_methodD(oneTimeSetUp, setUp):
    print("Running conftest demo1 method D")
