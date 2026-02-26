"""
Реалізувати функцію `sum_numbers_in_list(input_list)`, яка приймає список рядків, 
де кожен рядок містить числа, розділені комами. Функція повинна повертати список 
із сум чисел для кожного рядка або відповідне повідомлення про помилку у 
випадку некоректних даних.

#### **Приклади виклику функції:**
```python
sum_numbers_in_list(["1,2,3", "4,0,6"])  # [6, 10]
sum_numbers_in_list(["1,2,3", "asas7,8,9", "4,0,6"])  # [6, "Не можу це зробити!", 10]
sum_numbers_in_list(["1,2,3,4", 7])  # [10, "Не можу це зробити! AttributeError"]
sum_numbers_in_list([])  # ValueError
sum_numbers_in_list("21")  # ValueError
```
"""


def sum_numbers_in_list(string_list: list):
    """Повертає список сум чисел зі списку строк,
    які складаються з чисел, розділених комою."""
    if not isinstance(string_list, list) or len(string_list) == 0:
        raise ValueError("Очікується непорожній список")

    result = []

    for item in string_list:
        try:
            parts = item.split(",")

            numbers = []
            for part in parts:
                number = int(part)
                numbers.append(number)

            row_sum = sum(numbers)
            result.append(row_sum)

        except AttributeError:
            result.append("Не можу це зробити! AttributeError")

        except ValueError:
            result.append("Не можу це зробити!")

    return result

if __name__ == "__main__":
    print(sum_numbers_in_list(["1,2,3", "4,0,6"]))
    print(sum_numbers_in_list(["1,2,3", "4/0,6", "asas7,8,9"]))
    """
    sum_numbers_in_list(["1,2,3", "4,0,6"])  # [6, 10]
    sum_numbers_in_list(["1,2,3", "asas7,8,9", "4,0,6"])  # [6, "Не можу це зробити!", 10]
    sum_numbers_in_list(["1,2,3,4", 7])  # [10, "Не можу це зробити! AttributeError"]
    sum_numbers_in_list([])  # ValueError
    sum_numbers_in_list("21")  # ValueError
    """
