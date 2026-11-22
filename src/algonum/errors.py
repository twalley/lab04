class AlgonumError(Exception):
    """Базовое исключение для всего пакета algonum"""

    pass


class InvalidInputError(AlgonumError):
    """Ошибка при неверном вводе"""

    pass


class EmptyStructureError(AlgonumError):
    """Ошибка при операции над пустой структурой данных"""

    pass
