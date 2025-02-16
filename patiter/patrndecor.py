from typing import Callable

# Базовая функция
def simple_function() -> str:
    return "dnakjdnajdnja"

# Декоратор, добавляющий восклицательный знак
def exclamation_decorator(func: Callable[[], str]) -> Callable[[], str]:
    def wrapper() -> str:
        return func() + "1191191919"
    return wrapper

# Декоратор, добавляющий обрамление звездочками
def star_decorator(func: Callable[[], str]) -> Callable[[], str]:
    def wrapper() -> str:
        return "11111 " + func() + " jjjjjjjj"
    return wrapper

# Применение декораторов
@exclamation_decorator
@star_decorator
def decorated_function() -> str:
    return simple_function()

# Пример использования
print(decorated_function())
