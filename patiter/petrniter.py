from typing import Iterator

class ExpressionIterator:
    def __init__(self, expression: str):
        self.tokens = expression.replace(" ", "")  # Убираем пробелы
        self.index = 0

    def __iter__(self) -> Iterator[str]:
        return self

    def __next__(self) -> str:
        if self.index >= len(self.tokens):
            raise StopIteration
        
        if self.tokens[self.index] in '+-':  # Возвращаем операцию
            token = self.tokens[self.index]
            self.index += 1
            return token
        
        start = self.index
        while self.index < len(self.tokens) and self.tokens[self.index].isdigit():
            self.index += 1
        
        return self.tokens[start:self.index]  # Возвращаем число

# Функция для вычисления результата выражения
def evaluate_expression(expression: str) -> int:
    iterator = ExpressionIterator(expression)
    result = int(next(iterator))  # Первое число
    
    for token in iterator:
        operator = token
        number = int(next(iterator))
        if operator == '+':
            result += number
        elif operator == '-':
            result -= number
    
    return result

# Пример использования
expression = "12 + 34 - 5 + 67"
result = evaluate_expression(expression)
print(result)
