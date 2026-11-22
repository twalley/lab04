import pytest
from algonum import bubble_sort, merge_sort


# parametrize запускает каждый тест дважды для bubble_sort и merge_sort
@pytest.mark.parametrize("sort_func", [bubble_sort, merge_sort])
class TestSorting:
    """тесты для сортировок"""

    def test_empty_list(self, sort_func):
        """пустой список остается пустым"""
        assert sort_func([]) == []

    def test_single_element(self, sort_func):
        """список из одного элемента"""
        assert sort_func([42]) == [42]

    def test_already_sorted(self, sort_func):
        """уже отсортированный список"""
        assert sort_func([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_reverse_sorted(self, sort_func):
        """обратно отсортированный список"""
        assert sort_func([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_duplicates(self, sort_func):
        """список с дубликатами"""
        assert sort_func([3, 1, 2, 1, 3, 2]) == [1, 1, 2, 2, 3, 3]

    def test_negative_numbers(self, sort_func):
        """список с отрицательными числами"""
        assert sort_func([-3, -1, -2, 0, 1]) == [-3, -2, -1, 0, 1]

    def test_all_same(self, sort_func):
        """все элементы одинаковые"""
        assert sort_func([7, 7, 7, 7]) == [7, 7, 7, 7]

    def test_does_not_modify_input(self, sort_func):
        """входной список не должен изменяться"""
        original = [3, 1, 2]
        sort_func(original)
        assert original == [3, 1, 2]  # проверяем, что не поменялся

    def test_large_random(self, sort_func):
        """большой случайный список совпадает с эталоном"""
        import random

        rng = random.Random(42)
        arr = [rng.randint(-1000, 1000) for _ in range(100)]
        expected = sorted(arr)
        assert sort_func(arr) == expected

    def test_two_elements(self, sort_func):
        """два элемента"""
        assert sort_func([2, 1]) == [1, 2]
        assert sort_func([1, 2]) == [1, 2]

    def test_wrong_type_raises_error(self, sort_func):
        """неправильный тип вызывает ошибку"""
        with pytest.raises(TypeError):
            sort_func("не список")

        with pytest.raises(TypeError):
            sort_func(123)
