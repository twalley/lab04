from .errors import InvalidInputError


def ways_iterative(n: int) -> int:
    """
    двигаемся снизу вверх по лестнице, запоминая два последних значения
    для экономии памяти
    ways(n) = ways(n-1) + ways(n-2)
    ways(0) = 1 - стоим на земле — ничего не делать
    ways(1) = 1 - только один шаг
    ways(2) = 2 - два шага по 1 или один шаг на 2
    """
    # проверяем, что ввод корректный
    if not isinstance(n, int):
        raise InvalidInputError(f"Должно быть целое число, получено: {type(n).__name__}")
    if n < 0:
        raise InvalidInputError(f"Номер ступеньки не может быть отрицательным: {n}")

    # базовые случаи
    if n == 0:
        return 1  # стоим на земле — 1 способ
    if n == 1:
        return 1  # только один шаг

    # a — ways(i-2), b — ways(i-1)
    a = 1
    b = 1
    # идём от 2 до n
    for i in range(2, n + 1):
        # новое значение
        c = a + b
        a = b
        b = c
    # в конце b содержит ways(n)
    return b


def ways_recursive(n: int, _memo: dict | None = None) -> int:
    """
    рекурсивное решение лестницы с помощью
    запоминания уже посчитанных значений,
    чтобы не считать одно и то же много раз,
    чтобы не тратилось много времени
    ways(n) = ways(n-1) + ways(n-2)
    ways(0) = 1 - стоим на земле — ничего не делать
    ways(1) = 1 - только один шаг
    ways(2) = 2 - два шага по 1 или один шаг на 2
    """
    # проверяем ввод
    if not isinstance(n, int):
        raise InvalidInputError(f"Ожидается целое число, получено: {type(n).__name__}")
    if n < 0:
        raise InvalidInputError(f"Номер ступеньки не может быть отрицательным: {n}")

    # создаем словарь для запоминания уже посчитанных значений, если его еще нет
    if _memo is None:
        _memo = {}

    # если уже считали это значение — возвращаем из памяти
    if n in _memo:
        return _memo[n]

    if n == 0:
        result = 1
    elif n == 1:
        result = 1
    else:
        # рекурсия ways(n) = ways(n-1) + ways(n-2)
        result = ways_recursive(n - 1, _memo) + ways_recursive(n - 2, _memo)

    # запоминаем результат, чтобы не считать снова
    _memo[n] = result

    return result
