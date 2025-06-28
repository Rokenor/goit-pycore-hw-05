import re

def generator_numbers(text):
    # Паттерн для визначення числа
    pattern = r"(?<=\s)\d*[.]?\d+(?=\s)"

    # Цикл для проходу по тексту та створення генератора
    for match in re.finditer(pattern, text):
        number_str = match.group(0)
        yield float(number_str)

def sum_profit(text, func):
    result = 0

    # Знаходження суми всіх чисел знайдених зовнішнею функцією
    for number in func(text):
        result += number
    
    return result

if __name__ == "__main__":
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}") # Виведе 1351.46