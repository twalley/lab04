from typing import Any

from .errors import EmptyStructureError


class Stack:
    """
    стек - последним зашел, первым вышел
    """

    def __init__(self):
        """создаём пустой стек, внутри используем обычный список"""

        self._items: list[Any] = []

    def push(self, item: Any) -> None:
        """
        кладёт элемент наверх стека
        """

        # append добавляет элемент в конец списка
        self._items.append(item)

    def pop(self) -> Any:
        """
        cнимает верхний элемент со стека и возвращает его
        """

        # проверяем что стек не пустой
        if len(self._items) == 0:
            raise EmptyStructureError("Нельзя снять элемент с пустого стека")

        # pop() у списка удаляет и возвращает последний элемент
        return self._items.pop()

    def peek(self) -> Any:
        """
        возвращает верхний элемент, не снимая его
        """

        # проверяем что стек не пустой
        if len(self._items) == 0:
            raise EmptyStructureError("Нельзя посмотреть верхний элемент пустого стека")

        # верх стека - последний элемент списка
        return self._items[-1]

    def __len__(self) -> int:
        """
        возвращает количество элементов в стеке
        """
        return len(self._items)

    def __bool__(self) -> bool:
        """
        возвращает True если стек не пустой, False если пустой
        """
        return len(self._items) > 0

    def __repr__(self) -> str:
        """
        красивое представление стека для отладки
        """
        return f"Stack({self._items})"
