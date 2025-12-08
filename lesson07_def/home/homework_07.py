# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while number * multiplier <= 25:
        result = number * multiplier
        # десь тут помилка, а може не одна
            # Enter the action to take if the result is greater than 25
        print(f"{number}x{multiplier}={result}")

        # Increment the appropriate variable
        multiplier += 1

print(f"Task 1:")
multiplication_table(3)

# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def add_two_numbers(c, d):
    return  c + d
result = add_two_numbers(9, 99)
print(f"Task 2: {result}")


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average(numbers):
    if not numbers:
        return 0
    total = sum(numbers)
    count = len(numbers)
    return total / count

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(Evgenii):
    return Evgenii[::-1]
print("Task 4:")
print(reverse_string("Evgenii"))


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
animals = ["tiger", "monkey", "boar", "squirrel"]

def find_longest_word(words):
    if not words:
        return ""

    longest = words[0]

    for word in words[1:]:
        if len(word) > len(longest):
            longest = word

    return longest
print("Task 5:")
print(f"Words: {animals}")
longest = find_longest_word(animals)
print(f"Longest word: {longest}")

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
print("Task 6:")
def find_substring(str1, str2):
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))  # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))  # поверне -1

# task 7 Повернути множину унікальних елементів зі списку numbers
def get_unique_elements(numbers):
    """
    Повертає множину унікальних елементів зі списку numbers.
    """
    return set(numbers)


print("\nTask 7:")
print("Задача: Знайти всі унікальні елементи у списку.")

small_list = [3, 1, 4, 5, 2, 5, 3]
unique_numbers = get_unique_elements(small_list)

print(f"Початковий список: {small_list}")
print(f"Унікальні елементи: {unique_numbers}")


# task 8 Повернути True, якщо список items містить дублікати
#     та False, якщо всі елементи унікальні
def has_duplicates(items):
    """
    Повертає True, якщо список items містить дублікати,
    та False, якщо всі елементи унікальні.
    """
    return len(items) != len(set(items))
print("\nTask 8:")
print("Задача: Перевірити, чи є в списку дублікати.")

big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]

print(f"Список: {big_list}")
print(f"Є дублікати? {has_duplicates(big_list)}")

# task 9  Повернути новий словник, де ключі та значення поміняні місцями
def invert_dict(input_dict):
    """
    Повертає новий словник, де ключі та значення поміняні місцями.
    """
    inverted = {}
    for key, value in input_dict.items():
        inverted[value] = key
    return inverted
# task 10 Знайти суму всіх парних чисел у списку.
def sum_of_even_numbers(numbers):
    """
    Повертає суму всіх парних чисел у списку numbers.
    Якщо парних чисел немає — повертає 0.
    """
    total = 0
    for num in numbers:
        if num % 2 == 0:   # перевіряємо, чи число парне
            total += num
    return total
print("\nTask 10:")
print("Задача: Знайти суму всіх парних чисел у списку.")

nums = [1, 2, 3, 4, 5, 6]
result = sum_of_even_numbers(nums)

print(f"Список: {nums}")
print(f"Сума парних чисел: {result}")
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обов'язково документуйте функції та дайте зрозумілі імена змінним.
"""