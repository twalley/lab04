from algonum import (
    almost_sorted_array,
    many_duplicates_array,
    random_array,
    reverse_sorted_array,
    sorted_array,
)


class TestGenerators:
    """тесты для генераторов массивов"""

    def test_random_array_length(self):
        """длина массива равна n"""
        assert len(random_array(10)) == 10
        assert len(random_array(0)) == 0

    def test_random_array_seed_reproducible(self):
        """две генерации с одним seed дают одинаковый результат"""
        arr1 = random_array(100, seed=42)
        arr2 = random_array(100, seed=42)
        assert arr1 == arr2

    def test_random_array_different_seeds(self):
        """две генерации с разными seed дают разный результат"""
        arr1 = random_array(100, seed=1)
        arr2 = random_array(100, seed=2)
        assert arr1 != arr2

    def test_sorted_array_is_sorted(self):
        """отсортированный массив действительно отсортирован"""
        arr = sorted_array(50, seed=42)
        assert arr == sorted(arr)

    def test_reverse_sorted_array(self):
        """обратно отсортированный массив"""
        arr = reverse_sorted_array(50, seed=42)
        assert arr == sorted(arr, reverse=True)

    def test_almost_sorted_mostly_sorted(self):
        """почти отсортированный массив"""
        n = 100
        arr = almost_sorted_array(n, swaps=2, seed=42)
        sorted_arr = sorted(arr)

        # считаем сколько элементов не на своем месте
        misplaced = sum(1 for i in range(n) if arr[i] != sorted_arr[i])
        # после 2 обменов максимум 4 элемента не на месте
        assert misplaced <= 4

    def test_many_duplicates_few_unique(self):
        """массив с дубликатами имеет мало уникальных значений"""
        arr = many_duplicates_array(1000, unique=5, seed=42)
        assert len(set(arr)) <= 5

    def test_empty_array(self):
        """пустой массив"""
        assert random_array(0) == []
        assert sorted_array(0) == []

    def test_single_element(self):
        """массив из одного элемента"""
        arr = random_array(1, seed=42)
        assert len(arr) == 1

    def test_generators_dont_use_global_random(self):
        """
        генераторы не должны зависеть от глобального состояния random
        создаем свой генератор и проверяем, что он не влияет на другие
        """
        import random

        # сохраняем состояние глобального генератора
        state_before = random.getstate()

        # вызываем наши генераторы
        random_array(100, seed=42)
        sorted_array(100, seed=42)

        # проверяем, что глобальное состояние не изменилось
        state_after = random.getstate()
        assert state_before == state_after
