from app import add_numbers

def test_add_numbers_success():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0

def test_add_numbers_failure():
    assert add_numbers(2, 2) != 5