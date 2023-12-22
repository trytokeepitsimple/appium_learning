def setup_module(module):
    print("This is defined at module level - > This will run before running any test in module")


def teardown_module(module):
    print("This is defined at module level -> This will run after running all tests in module")





def setup_function(function):
    # Actions to be performed before each test function
    # For instance, setting up resources, initializing variables, etc.
    print("Setup function - This will run before each test function")


def teardown_function(function):
    print("This is tear down function")
def test_example_1():
    assert True

def test_example_2():
    assert True
