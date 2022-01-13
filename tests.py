import pytest
from allpairspy import AllPairs
from _pytest.outcomes import Failed

from main import premium, premium_mod

salary_positive_values = [70000, 100000, 750000]
level_positive_values = [7, 10, 17]
salary_negative_values = [69000, 750001, "string"]
level_negative_values = [6, 17.1, 18, "string"]

review_positive_values = [1, 2.5, 5, ]
review_negative_values = [0, 5.1, 6, "string"]


@pytest.mark.parametrize(["salary", "level"], [(-1, -1), (70000, "str")])
def test_premium_and_mod(salary, level):
    with pytest.raises((ValueError, TypeError)):
        premium(salary, level)
        premium_mod(salary, level)


@pytest.mark.parametrize(["salary", "level"], [
    value_list for value_list in AllPairs([salary_negative_values, level_negative_values])])
def test_premium_negative(salary, level):
    with pytest.raises((ValueError, TypeError)):
        premium(salary, level)


@pytest.mark.parametrize(["salary", "level"], [
    value_list for value_list in AllPairs([salary_positive_values, level_positive_values])])
def test_premium_positive(salary, level):
    assert premium(salary, level) is not None


@pytest.mark.parametrize(["salary", "level", "review"], [
    value_list for value_list in AllPairs([salary_positive_values, level_positive_values, review_negative_values])])
def test_premium_mod_negative(salary, level, review):
    with pytest.raises((ValueError, TypeError)):
        premium_mod(premium(salary, level), review)


@pytest.mark.parametrize(["salary", "level", "review"], [
    value_list for value_list in AllPairs([salary_positive_values, level_positive_values, review_positive_values])])
def test_premium_mod_positive(salary, level, review):
    assert premium_mod(premium(salary, level), review) is not None
