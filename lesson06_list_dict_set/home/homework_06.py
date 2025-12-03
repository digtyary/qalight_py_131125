# task 1. Знайдіть всі унікальні елементи в списку small_list
small_list = [3, 1, 4, 5, 2, 5, 3]
unique_from_small = set(small_list)
print("Task 1 – унікальні елементи:", unique_from_small)

# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list
total = sum(small_list)    # сума всіх елементів
count = len(small_list)    # кількість елементів
average = total / count    # середнє арифметичне
print("Task 2 – середнє:", average)


# task 3. Перевірте, чи є в списку big_list дублікати
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
has_duplicates = len(big_list) != len(set(big_list))
print("Task 3 – є дублікати?:", has_duplicates)


# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}

max_key = max(add_dict, key=add_dict.get)
print("Task 4 – ключ з максимальним значенням:", max_key, "=>", add_dict[max_key])

# task 5. Створіть новий словник, в якому ключі та значення base_dict будуть
# замінені місцями ({'Ukraine':'contry'...})

base_dict = {'contry': 'Ukraine', 'continent': 'Europe', 'size': 123}
inverted_dict = {}
for key, value in base_dict.items():
    inverted_dict[value] = key
print("Task 5 – інвертований base_dict:", inverted_dict)

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх
sum_dict = {}
for key, value in base_dict.items():
    sum_dict[key] = value

for key, value in add_dict.items():
    if key in sum_dict:
        sum_dict[key] = str(sum_dict[key]) + str(value)
    else:
        sum_dict[key] = value
print("Task 6 – sum_dict:", sum_dict)


# task 7.
line = "Створіть множину всіх символів, які входять у заданий рядок"
char_set = set(line)
print("Task 7 – множина символів:", char_set)


# task 8. Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}

unique_elements = []

for num in set_1:
    if num not in set_2:
        unique_elements.append(num)

for num in set_2:
    if num not in set_1:
        unique_elements.append(num)

result = sum(unique_elements)

print("Task 8 – унікальні числа, які є тільки в одній множині:", unique_elements)
print("Task 8 – сума цих чисел:", result)

# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]

person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]

list_1 = [1, 2, 3, 4]
list_2 = [3, 4, 5, 6]
combined = list_1 + list_2
unique_once = []
for num in combined:
    if combined.count(num) == 1:
        unique_once.append(num)
result_set = set(unique_once)
print("Task 9 – елементи, які зустрічаються тільки один раз:", result_set)

# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}

person_list = [
    ('Alice', 25),
    ('Boby', 19),
    ('Charlie', 32),
    ('David', 28),
    ('Emma', 22),
    ('Frank', 45)
]

age_ranges = {}

for name, age in person_list:
    lower_bound = (age // 10) * 10
    upper_bound = lower_bound + 9
    range_key = f"{lower_bound}-{upper_bound}"
    if range_key not in age_ranges:
        age_ranges[range_key] = []
    age_ranges[range_key].append(name)
print("Task 10 – групування по вікових діапазонах:", age_ranges)
