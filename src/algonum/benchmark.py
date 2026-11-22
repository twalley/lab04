import math
import time

from .generators import (
    almost_sorted_array,
    many_duplicates_array,
    random_array,
    reverse_sorted_array,
    sorted_array,
)
from .sorting import bubble_sort, merge_sort

# маленькие размеры тестируем обе сортировки
SMALL_SIZES = [100, 1000, 10000]

# большие размеры bubble_sort только на отсортированных
LARGE_SIZES = [100000, 1000000]


def _measure_time(func, arr: list[int], repeats: int = 5) -> float:
    """
    измеряет среднее время выполнения func на массиве arr
    func - функция сортировки
    arr - исходный массив, не меняется
    repeats - количество повторов
    """
    times = []

    for _ in range(repeats):
        # создаем новую копию для каждого запуска
        test_arr = list(arr)

        # время до (засечь секундомер)
        start = time.perf_counter()

        # запускаем функцию
        func(test_arr)

        # время после
        end = time.perf_counter()

        # сохраняем время одного запуска
        times.append(end - start)

    # возвращаем среднее время
    return sum(times) / len(times)


def run_benchmark(sizes: list[int] = None, repeats: int = 5, seed: int = 42) -> dict:
    """
    запускает бенчмарк сортировок на разных размерах массивов
    sizes - список размеров массивов
    repeats - количество повторов для каждого замера
    seed - для инициализации массивов
    """
    if sizes is None:
        sizes = SMALL_SIZES + LARGE_SIZES

    # список функций для тестирования
    functions = [
        ("bubble_sort", bubble_sort),
        ("merge_sort", merge_sort),
    ]

    # список типов массивов
    array_types = [
        ("random", random_array),
        ("sorted", sorted_array),
        ("reverse", reverse_sorted_array),
        ("almost_sorted", almost_sorted_array),
        ("many_duplicates", many_duplicates_array),
    ]

    # словарь для хранения результатов
    # results[func_name][array_type][size] = время
    results = {}

    # проходим по всем функциям
    for func_name, func in functions:
        results[func_name] = {}

        # проходим по всем типам массивов
        for arr_type, generator in array_types:
            results[func_name][arr_type] = {}

            # проходим по всем размерам
            for size in sizes:
                if func_name == "bubble_sort" and size in LARGE_SIZES and arr_type != "sorted":
                    results[func_name][arr_type][size] = None
                    continue

                # генерируем массив один раз
                base_arr = generator(size, seed=seed)

                # измеряем время
                avg_time = _measure_time(func, base_arr, repeats=repeats)

                # сохраняем результат
                results[func_name][arr_type][size] = avg_time

    return results


def format_benchmark_markdown(results: dict) -> str:
    """
    Форматирует результаты бенчмарка в markdown-таблицу
    """
    lines = []

    # заголовок таблицы с фиксированной шириной колонок
    lines.append("| Тип данных             |   Размер | Bubble Sort (с)  | Merge Sort (с)   |")
    lines.append("|------------------------|----------|------------------|------------------|")

    # проходим по всем типам массивов
    for arr_type in ["random", "sorted", "reverse", "almost_sorted", "many_duplicates"]:
        # собираем все размеры из результатов
        all_sizes = set()
        if arr_type in results.get("bubble_sort", {}):
            all_sizes.update(results["bubble_sort"][arr_type].keys())
        if arr_type in results.get("merge_sort", {}):
            all_sizes.update(results["merge_sort"][arr_type].keys())

        # сортируем размеры по возрастанию
        sorted_sizes = sorted(all_sizes)

        # для каждого размера создаем строку таблицы
        for size in sorted_sizes:
            # получаем время bubble_sort
            bubble_time = results.get("bubble_sort", {}).get(arr_type, {}).get(size)
            if bubble_time is not None:
                bubble_str = f"{bubble_time:.6f}"  # показывает 6 цифр после точки
            else:
                bubble_str = "-"

            # получаем время merge_sort
            merge_time = results.get("merge_sort", {}).get(arr_type, {}).get(size)
            if merge_time is not None:
                merge_str = f"{merge_time:.6f}"  # показывает 6 цифр после точки
            else:
                merge_str = "-"

            # создаем строку таблицы
            line = f"| {arr_type:<22} | {size:>8} | {bubble_str:>16} | {merge_str:>16} |"
            lines.append(line)

    # соединяем все строки в одну большую строку
    return "\n".join(lines)


def analyze_complexity(results: dict) -> str:
    """
    анализирует результаты и сопоставляет с теоретической сложностью
    """
    lines = []
    lines.append("СЛОЖНОСТЬ СОРТИРОВОК\n")

    # берем тип массива random для анализа
    arr_type = "random"

    for sort_name in ["bubble_sort", "merge_sort"]:
        lines.append(f"- {sort_name}\n")

        # получаем времена для всех размеров
        times = []
        for size, time_val in results.get(sort_name, {}).get(arr_type, {}).items():
            if time_val is not None and time_val > 0:
                times.append((size, time_val))

        # сортируем по размеру
        times.sort()

        if len(times) < 2:
            lines.append("Недостаточно данных для анализа\n")
            continue

        # сравниваем каждый размер с предыдущим
        for i in range(1, len(times)):
            prev_size, prev_time = times[i - 1]
            curr_size, curr_time = times[i]

            size_ratio = curr_size / prev_size
            time_ratio = curr_time / prev_time

            # теоретическое увеличение для O(n²)
            expected_quadratic = size_ratio**2

            # теоретическое увеличение для O(n log n)
            expected_nlogn = (curr_size * math.log2(curr_size)) / (prev_size * math.log2(prev_size))

            lines.append(f"\tПереход от {prev_size} к {curr_size} элементам\n")
            lines.append(f"\t\t* Размер увеличился в {size_ratio:.0f} раз")
            lines.append(f"\t\t* Время увеличилось в {time_ratio:.1f} раз")
            lines.append(
                f"\t\t*Если б сложность была O(n²), время выросло б в {expected_quadratic:.0f} раз"
            )
            lines.append(
                f"\t\t*Если б сложность была O(n log n), время выросло б в {expected_nlogn:.1f} раз"
            )
            lines.append("")

        # общий вывод по сортировке
        first_size, first_time = times[0]
        last_size, last_time = times[-1]

        size_ratio = last_size / first_size
        time_ratio = last_time / first_time

        expected_quadratic = size_ratio**2
        expected_nlogn = (last_size * math.log2(last_size)) / (first_size * math.log2(first_size))

        diff_quadratic = abs(time_ratio - expected_quadratic)
        diff_nlogn = abs(time_ratio - expected_nlogn)

        if diff_quadratic < diff_nlogn:
            lines.append("Вывод: Рост времени ближе к O(n²) — квадратичная сложность")
        else:
            lines.append(
                "Вывод: Рост времени ближе к O(n log n) — линейно-логарифмическая сложность"
            )
        lines.append("")

    return "\n".join(lines)


def save_benchmark_report(results: dict, filepath: str = "benchmark_report.md") -> None:
    """
    сохраняет полный отчёт бенчмарка в Markdown-файл (+2 балла за доп. задание)
    """
    report = "# Отчёт бенчмарка сортировок\n\n"
    report += format_benchmark_markdown(results)
    report += "\n\n"
    report += analyze_complexity(results)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"Отчёт сохранён в {filepath}")
