import pytest

@pytest.fixture
def setUp():
    print("Running method level setup")
    yield
    print("Running method level tearDown")

@pytest.fixture(scope="module")
def oneTimeSetUp():
    print("Running conftest demo one time setup")
    yield
    print("Running conftest demo one time tearDown")