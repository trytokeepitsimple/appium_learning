import pytest

@pytest.mark.functional
def test_function_one():
    print("F1")

@pytest.mark.regresation
def test_function_two():
    print("F2")

@pytest.mark.functional
def test_function_three():
    print("F3")