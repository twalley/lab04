import pytest
from algonum import InvalidInputError, ways_iterative, ways_recursive


# parametrize позволяет запустить один тест несколько раз с разными аргументами
@pytest.mark.parametrize("func", [ways_iterative, ways_recursive])
class TestWays:
    """тесты для функций подсчета способов подъема по лестнице"""

    def test_zero_steps(self, func):
        """на нулевую ступеньку - 1 способ"""
        assert func(0) == 1

    def test_one_step(self, func):
        """на первую ступеньку - 1 способ"""
        assert func(1) == 1

    def test_two_steps(self, func):
        """на вторую ступеньку - 2 способа"""
        assert func(2) == 2

    def test_three_steps(self, func):
        """на третью ступеньку - 3 способа"""
        assert func(3) == 3

    def test_five_steps(self, func):
        """для n=5 (должно быть 8)"""
        assert func(5) == 8

    def test_ten_steps(self, func):
        """для n=10 (должно быть 89)"""
        assert func(10) == 89

    def test_negative_raises_error(self, func):
        """отрицательное число должно вызывать ошибку"""
        with pytest.raises(InvalidInputError):
            func(-1)

    def test_wrong_type_raises_error(self, func):
        """не целое число должно вызывать ошибку"""
        with pytest.raises(InvalidInputError):
            func(3.5)

    def test_string_raises_error(self, func):
        """строка должна вызывать ошибку"""
        with pytest.raises(InvalidInputError):
            func("5")


def test_iterative_and_recursive_match():
    """итеративная и рекурсивная версии дают одинаковый результат"""
    # проверяем на нескольких значениях
    for n in range(20):
        assert ways_iterative(n) == ways_recursive(n)
