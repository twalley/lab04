from algonum import (
    run_benchmark,
)


class TestBenchmark:
    """тесты для бенчмарка"""

    def test_run_benchmark_returns_dict(self):
        """бенчмарк возвращает словарь"""
        # запускаем бенчмарк на маленьких размерах для скорости
        results = run_benchmark(sizes=[100, 1000], repeats=2, seed=42)

        # проверяем, что результат — словарь
        assert isinstance(results, dict)

    def test_benchmark_has_both_sorts(self):
        """в результатах есть обе сортировки"""
        results = run_benchmark(sizes=[100], repeats=2, seed=42)

        # проверяем, что есть bubble_sort и merge_sort
        assert "bubble_sort" in results
        assert "merge_sort" in results

    def test_benchmark_has_all_array_types(self):
        """в результатах есть все типы массивов"""
        results = run_benchmark(sizes=[100], repeats=2, seed=42)

        # список ожидаемых типов массивов
        expected_types = [
            "random",
            "sorted",
            "reverse",
            "almost_sorted",
            "many_duplicates",
        ]

        # проверяем каждый тип для обеих сортировок
        for sort_name in ["bubble_sort", "merge_sort"]:
            for arr_type in expected_types:
                assert arr_type in results[sort_name], f"Нет типа {arr_type} в {sort_name}"

    def test_benchmark_has_requested_sizes(self):
        """в результатах есть все запрошенные размеры"""
        sizes = [100, 500, 1000]
        results = run_benchmark(sizes=sizes, repeats=2, seed=42)

        # проверяем, что все размеры есть в результатах
        for sort_name in ["bubble_sort", "merge_sort"]:
            for arr_type in results[sort_name]:
                for size in sizes:
                    assert size in results[sort_name][arr_type], f"Нет размера {size}"
