# Вправа 1: Проста математика
# print("\n=== ВПРАВА 1: Калькулятор ===")
# print("Створіть простий калькулятор для двох чисел і двох дій")
# print("Підтримувані операції: +, -")

print("\n=== Task 1: Calculator ===")

num1 = float(input("Введіть перше число: "))
operation = input("Введіть операцію (+, -, ): ")
num2 = float(input("Введіть друге число: "))

if operation == "+":
    print(f"Result: {num1 + num2}")
elif operation == "-":
    print(f"Result: {num1 - num2}")
else:
    print("Unknown operation")


# Вправа 2: Перевірка паролю
# print("\n=== Task2: Password Check  ===")
# print("Створіть систему перевірки паролю")
# print("Пароль повинен містити принаймні 8 символів")

password = input("Enter password: ")

if len(password) >= 8:
    print("Password accepted")
else:
    print("Password is too short")


# Вправа 3: Визначення високосного року
# print("\n=== ВПРАВА 3: Високосний рік ===")
# print("Рік є високосним, якщо:")
# print("- Ділиться на 4 І не ділиться на 100")
# print("- АБО ділиться на 400")

print("\n=== Task3: Leap Year ===")
#
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("This is a leap year")
else:
    print("This is not a leap year")


# Вправа 4: Лічильник голосних
print("\n=== Task 4: counting ===")
# print("Підрахуйте кількість голосних у рядку")
#
text = input("Enter text: ").lower()
vowels = "аеиіїоуюя"
count = 0
# код тут
for char in text:
    if char in vowels:
        count += 1

print(f"Number of vowels: {count}")
#
#
#
# Вправа 5: Гра 
print("\n=== Task 5: Game===")
# """
# Уявіть, що інопланетянина з кольором alien_color щойно збили в грі.
# Створіть змінну під назвою alien_color і призначте їй значення 'green', 'yellow', або 'red'.
# Напишіть оператор if, щоб перевірити, чи колір прибульця 'green'.
# Якщо колір прибульця green, надрукуйте, що гравець щойно заробив 5 балів.
# Якщо колір прибульця yellow, надрукуйте, що гравець щойно заробив 10 балів.
# Якщо колір прибульця red - надрукуйте, що гравець щойно заробив 15 балів.
# Перевірте роботу гри самостійно, змінюючи значення alien_color
# """
alien_color = input("Enter alien color (green, yellow, red): ").lower()

if alien_color == "green":
    print("You earned 5 points!")
elif alien_color == "yellow":
    print("You earned 10 points!")
elif alien_color == "red":
    print("You earned 15 points!")
else:
    print("Unknown alien color")
#
#

# Вправа 6: Піцерія *
print("\n=== Task  6: Начинки для піци (pizza_topping) ===")
# """  Начинки для піци (pizza_topping): напишіть цикл, який пропонує користувачеві ввести ряд начинок
# для піци, доки він не введе значення 'quit'. Коли вони введуть кожну начинку,
# надрукуйте повідомлення про те, що ви додасте цю начинку до їхньої піци.
# """
while True:
    topping = input("Add topping (or 'quit' to stop): ")

    if topping == "quit":
        break

    print(f"Adding topping: {topping}")

#

# Вправа 7: Зворотний порядок цифр
# print("\n=== Task 7: Reverse Digits ===")
# print("Виведіть цифри числа у зворотному порядку")

number = input("Enter a number: ")

print(number[::-1])


# Вправа 8: Пошук максимального числа
# print("\n=== Task 8: Find Maximum Until 0 ===")
# print("Знайдіть найбільше число серед введених")
# print("Введіть 0 для завершення")

num = int(input("Enter a number (0 to stop): "))

max_number = num

while num != 0:
    num = int(input("Enter a number (0 to stop): "))
    if num > max_number:
        max_number = num

print("Max number:", max_number)
#
#
#
# Вправа 9: Виключення зі списку
print("\n=== Task 9: Skip ===")
# """  Задача з використанням циклу for та continue. Задано список фруктів 'fruits'
# потрібно вивести на екран всі елементи списку, окрім "orange".
# """
fruits = ["apple", "banana", "orange", "grape", "mango"]

for fruit in fruits:
    if fruit == "orange":
        continue
    print(fruit)



# Вправа 10: Вираз в один рядок
print("\n=== Task 10: List of squares ===")
# """  Задано список чисел numbers, потрібно знайти список квадратів
# парних чисел зі списку. Спробуйте використати if та цикл for в один рядок.
# """
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []


for number in numbers:
    if number % 2 == 0:
        result.append(number * number)

print(result)
