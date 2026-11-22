# Этот файл запускается командой "python -m algonum"

from .benchmark import (
    analyze_complexity,
    format_benchmark_markdown,
    run_benchmark,
    save_benchmark_report,
)
from .recurrence import ways_iterative, ways_recursive
from .sorting import bubble_sort, merge_sort
from .stack import Stack


def main():
    """демонстрация работы пакета"""

    print("Алгоритмический мини-пакет\n")

    # рекуррентная лестница
    print("\n1 число способов подъёма по лестнице\n")

    # gроверяем разные значения n
    for n in [0, 1, 2, 5, 10, 20]:
        iter_result = ways_iterative(n)
        rec_result = ways_recursive(n)
        print(f"   шагов - {n:2d}: итеративно = {iter_result:6d}, рекурсивно = {rec_result:6d}")

    # cортировки
    print("\n2 cортировки\n")

    # создаем тестовый массив
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"\tисходный массив: {arr}")
    print(f"\tbubble sort: {bubble_sort(arr)}")
    print(f"\tmerge sort: {merge_sort(arr)}")
    print(f"\tисходный не изменился: {arr}")  # проверяем, что не поменялся

    # стек
    print("\n3 стек\n")

    # создаем пустой стек
    stack = Stack()
    print(f"\tпустой стек: {stack}, len = {len(stack)}, bool = {bool(stack)}")

    # кладем элементы
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"\tпосле push(1,2,3): {stack}, len = {len(stack)}")

    # смотрим верхний элемент
    print(f"\tpeek(верхний): {stack.peek()}")

    # снимаем верхний элемент
    print(f"\tpop: {stack.pop()}")
    print(f"\tпосле pop: {stack}")

    # benchmark
    print("\n4. Benchmark\n")
    results = run_benchmark(repeats=5, seed=42)

    # выводим таблицу с результатами в консоль
    print(format_benchmark_markdown(results))
    # выводим анализ сложности в консоль
    print("\n")
    print(analyze_complexity(results))
    # сохраняем полный отчет в файл benchmark_report.md
    save_benchmark_report(results, "benchmark_report.md")


if __name__ == "__main__":
    main()
