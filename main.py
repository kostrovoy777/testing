import random
import pytest
from allpairspy import AllPairs


def premium(salary: int, level: int) -> float:
    if salary < 70000 or 750000 < salary:
        raise ValueError('Salary must be between 70000 and 750000')
    if level < 7 or 17 < level:
        raise ValueError('Level must be between 7 and 17')
    if level < 10:
        return 0.05 * salary
    if 10 <= level < 13:
        return 0.1 * salary
    if 13 <= level < 15:
        return 0.15 * salary
    if 15 <= level:
        return 0.2 * salary


def premium_mod(premium: float, review: float) -> float:
    if review < 1 or 5 < level:
        raise ValueError('Review must be between 1 and 5')
    if premium < 0:
        raise ValueError('Premium cant be negative')
    if review < 2:
        return 0
    if 2 <= review < 2.5:
        return 0.25 * premium
    if 2.5 <= review < 3:
        return 0.5 * premium
    if 3 <= review < 3.5:
        return premium
    if 3.5 <= review < 4:
        return 1.5 * premium
    if 4 <= review:
        return 2 * premium


if __name__ == '__main__':
    random.seed()
    salary = random.randint(70000, 750000)
    level = random.randint(7, 17)
    review = random.randint(10, 50) / 10
    total = salary + premium(salary, level) + premium_mod(premium(salary, level), review)
    print("Salary: {}, level: {}, review: {}. Total money: {}".format(salary, level, review, total))
