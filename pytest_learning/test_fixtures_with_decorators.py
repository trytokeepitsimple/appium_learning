import pytest


#defining fixtures with decorators
#fixture defined at module level
@pytest.fixture(scope='module')
def setup():
    print("creating DB Connection")
    yield
    #yield will act like as teardown_function
    print("Closing DB Connection")

#fixture defined at function level
@pytest.fixture(scope='function')
def before():
    print("This will be called before any test function")
    yield
    # yield will act like as teardown_function
    print("This will run after each test function")

#calling fixture
# def test_one(before):
#     print("Test 1")
#
# def test_two(before,setup):
#     print("Test 2")



#another way to use fixtures

@pytest.mark.usefixtures("setup","before")
def test_one():
    print("Function 1")



@pytest.mark.usefixtures("before")

def test_two():
    print("function 2")