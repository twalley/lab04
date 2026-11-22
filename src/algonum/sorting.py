def bubble_sort(arr: list[int]) -> list[int]:
    """
    сортировка пузырьком
    проходим много раз по массиву сравнивая соседнии значения,
    если предыдущее больше следующего меняем их местами (n^2)
    """
    # проверяем тип
    if not isinstance(arr, list):
        raise TypeError(f"Ожидается список, получено: {type(arr).__name__}")

    # создаем копию списка, не меняем исходный
    result = list(arr)
    n = len(result)

    for i in range(n):
        # если за проход не было обменов список уже отсортирован
        swapped = False

        # n - i - 1 потому что последние i элементов уже на месте
        for j in range(n - i - 1):
            # левый > правого, то меняем их местами
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        # за весь проход не было обменов выходим раньше
        if not swapped:
            break

    return result


def _merge(arr: list[int], left: list[int], right: list[int]) -> None:
    """
    сливает два отсортированных списка left и right в список arr
    """
    i = 0  # индекс в arr
    j = 0  # индекс в left
    k = 0  # индекс в right

    # пока есть элементы в двух списках берём меньший
    while j < len(left) and k < len(right):
        if left[j] <= right[k]:
            arr[i] = left[j]
            j += 1
        else:
            arr[i] = right[k]
            k += 1
        i += 1

    # дописываем остатки из left
    while j < len(left):
        arr[i] = left[j]
        j += 1
        i += 1

    # дописываем остатки из right
    while k < len(right):
        arr[i] = right[k]
        k += 1
        i += 1


def _merge_sort_inplace(arr: list[int]) -> None:
    """
    внутренняя рекурсивная функция сортировки слиянием
    """
    n = len(arr)

    # уже отсортирован
    if n <= 1:
        return

    # делим список пополам
    mid = n // 2
    left = arr[:mid]  # левая половина
    right = arr[mid:]  # правая половина

    # рекурсивно сортируем обе половины
    _merge_sort_inplace(left)
    _merge_sort_inplace(right)

    # сливаем две отсортированные половины обратно в arr
    _merge(arr, left, right)


def merge_sort(arr: list[int]) -> list[int]:
    """
    сортировка слиянием
    делим список пополам, сортируем каждую половину,
    потом сливаем две отсортированные половины в одну
    """
    # проверяем тип
    if not isinstance(arr, list):
        raise TypeError(f"Ожидается список, получено: {type(arr).__name__}")

    # создаем копию, меняя исходный
    result = list(arr)

    # запускаем рекурсивную сортировку
    _merge_sort_inplace(result)

    return result
