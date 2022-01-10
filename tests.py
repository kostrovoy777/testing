import pytest
from allpairspy import AllPairs
from _pytest.outcomes import Failed

from main import premium, premium_mod

salary_test_values = [69000, 70000, 100000, 750000, 750001, "string"]
level_test_values = [6, 7, 10, 17, 17.1, 18, "string"]
salary_values = [70000, 100000, 750000]
level_values = [7, 10, 17]
review_test_values = [0, 1, 2.5, 5, 5.1, 6, "string"]


def test_premium_value():
    with pytest.raises(ValueError):
        premium(100, 5)


def test_premium_type():
    with pytest.raises(TypeError):
        premium(100000, "str")


def test_premium_mod_value():
    with pytest.raises(ValueError):
        premium_mod(0, 10)


def test_premium_mod_type():
    with pytest.raises(TypeError):
        premium_mod(0, "str")


@pytest.mark.parametrize(["salary", "level"], [
    value_list for value_list in AllPairs([salary_test_values, level_test_values])])
def test_premium(salary, level):
    result = 0
    try:
        with pytest.raises(ValueError, TypeError):
            result = premium(salary, level)
            assert result != 0, "The value was not calculated"
    except Failed:
        assert result == 0


@pytest.mark.parametrize(["salary", "level", "review"], [
    value_list for value_list in AllPairs([salary_values, level_values, review_test_values])])
def test_premium_mod(salary, level, review):
    result = -1
    try:
        with pytest.raises(ValueError, TypeError):
            result = premium_mod(premium(salary, level), review)
            assert result != -1, "The value was not calculated"
    except Failed:
        assert result == -1