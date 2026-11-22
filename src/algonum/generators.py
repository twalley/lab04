import random


def random_array(n: int, seed: int | None = None) -> list[int]:
    """
    создает случайный массив из n целых чисел
    seed - число для инициализации генератора случайных чисел
    (если передать одно и то же — получится одинаковый массив)
    """

    # инициализируем генератор
    rng = random.Random(seed)

    # создаем список из n случайных чисел
    result = []

    for _ in range(n):
        # генерируем случайное число от -1000 до 1000
        random_number = rng.randint(-1000, 1000)

        # добавляем его в список
        result.append(random_number)

    # возвращаем готовый список
    return result


def sorted_array(n: int, seed: int | None = None) -> list[int]:
    """
    создает отсортированный по возрастанию массив
    """
    # берем случайный массив и сортируем его
    arr = random_array(n, seed)
    return sorted(arr)


def reverse_sorted_array(n: int, seed: int | None = None) -> list[int]:
    """
    создает массив, отсортированный по убыванию.
    """
    arr = random_array(n, seed)
    return sorted(arr, reverse=True)


def almost_sorted_array(n: int, swaps: int = 2, seed: int | None = None) -> list[int]:
    """
    создает почти отсортированный массив
    берем отсортированный и делаем несколько случайных обменов
    n - размер массива
    swap - количество случайных обменов
    seed - для инициализации
    """
    arr = sorted_array(n, seed)
    rng = random.Random(seed)

    # Делаем несколько случайных обменов
    for _ in range(swaps):
        i = rng.randint(0, n - 1)
        j = rng.randint(0, n - 1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr


def many_duplicates_array(n: int, unique: int = 5, seed: int | None = None) -> list[int]:
    """
    создает массив с большим количеством дубликатов
    n - размер массива
    unique - количество различных значений
    seed - для инициализации
    """
    rng = random.Random(seed)

    # создаём pool из unique различных значений
    pool = []

    for _ in range(unique):
        random_number = rng.randint(-1000, 1000)
        pool.append(random_number)

    # заполняем массив случайными значениями из пула
    result = []

    for _ in range(n):
        chosen_number = rng.choice(pool)
        result.append(chosen_number)

    return result
