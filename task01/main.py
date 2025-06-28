def caching_fibonacci():
    # Створюємо словник для кешування
    cache = {}

    def fibonacci(num):
        # Обробляємо базові значення
        if num <= 0: 
            return 0
        elif num == 1:
            return 1
        # Шукаємо значення в кеші та вертаємо його якщо воно там існує
        elif num in cache:
            return cache[num]
        # Визначаємо неіснуюче в кеші значення, збергігаємо його в кеш та вертаємо його
        else:
            cache[num] = fibonacci(num-1) + fibonacci(num-2)
            return cache[num]
    
    return fibonacci

if __name__ == "__main__":
    # Отримуємо функцію fibonacci
    fib = caching_fibonacci()
            
    # Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
    print(fib(10))  # Виведе 55
    print(fib(15))  # Виведе 610