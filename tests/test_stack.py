import pytest
from algonum import EmptyStructureError, Stack


class TestStack:
    """тесты для стека"""

    def test_empty_stack(self):
        """новый стек пустой"""
        stack = Stack()
        assert len(stack) == 0
        assert not stack  # bool(stack) == False

    def test_push_and_len(self):
        """после push длина увеличивается"""
        stack = Stack()
        stack.push(1)
        assert len(stack) == 1
        stack.push(2)
        assert len(stack) == 2

    def test_pop_returns_last(self):
        """pop возвращает последний добавленный элемент"""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        # последний добавленный (3), должен вернуться первым
        assert stack.pop() == 3
        assert stack.pop() == 2
        assert stack.pop() == 1

    def test_pop_decreases_len(self):
        """после pop длина уменьшается"""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.pop()
        assert len(stack) == 1

    def test_peek_does_not_remove(self):
        """peek возвращает верхний элемент, но не удаляет его"""
        stack = Stack()
        stack.push(42)

        assert stack.peek() == 42
        assert stack.peek() == 42  # второй раз тоже работает
        assert len(stack) == 1  # длина не изменилась

    def test_pop_empty_raises_error(self):
        """pop на пустом стеке вызывает ошибку"""
        stack = Stack()
        with pytest.raises(EmptyStructureError):
            stack.pop()

    def test_peek_empty_raises_error(self):
        """peek на пустом стеке вызывает ошибку"""
        stack = Stack()
        with pytest.raises(EmptyStructureError):
            stack.peek()

    def test_bool_true_when_not_empty(self):
        """непустой стек - это True"""
        stack = Stack()
        stack.push(1)
        assert bool(stack) is True

    def test_bool_false_when_empty(self):
        """пустой стек - это False"""
        stack = Stack()
        assert bool(stack) is False

    def test_mixed_operations(self):
        """смешанные операции push/pop"""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.pop()  # убираем 2
        stack.push(3)
        stack.push(4)

        # сейчас - [1, 3, 4] (снизу вверх)
        assert stack.pop() == 4
        assert stack.pop() == 3
        assert stack.pop() == 1

    def test_invariant_len_after_push_pop(self):
        """
        после push и pop длина должна вернуться к исходной
        тест инварианта структуры данных
        """
        stack = Stack()
        initial_len = len(stack)

        stack.push(10)
        stack.push(20)
        stack.pop()
        stack.pop()

        assert len(stack) == initial_len
