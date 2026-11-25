"""Модуль базових арифметичних операцій для демонстрації CI/CD."""


def add(a: float, b: float) -> float:
    """Обчислює суму двох чисел.

    Args:
        a: Перший доданок.
        b: Другий доданок.

    Returns:
        Сума a та b.
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """Обчислює різницю двох чисел.

    Args:
        a: Зменшуване.
        b: Від'ємник.

    Returns:
        Різниця a та b.
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """Обчислює добуток двох чисел.

    Args:
        a: Перший множник.
        b: Другий множник.

    Returns:
        Добуток a та b.
    """
    return a * b
