# task 01 == Виправте синтаксичні помилки
print("Hello", end = " ")
print("world!")

# task 02  == Виправте назви змінних, щоб текст виводився
hello = "Hello"
world = "world"
print(f"{hello} {world}!")

# task 03 == Зробіть так, щоб кількість бананів була
# завжди на чотири штуки більша, ніж яблук
apples = 1900
banana = apples + 4
print(apples, banana)



# task 04 == виправте назви змінних
side_number_1 = 1
side_number_2 = 2
side_number_3 = 3
side_number_4 = 4

# task 05 == Порахуйте периметр фігури з task 04
# та виведіть його для користувача
perimetery = side_namber_1 + side_namber_2 + side_namber_3 + side_namber_4
print(f" Периметр  геометричної фігури: {perimetery}")


"""
    # Задачі 06 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""

# task 06
"""
У Оксани було 20 марок із серії «Мистецтво» 
і 7 марок із серії «Звірі».
5 марок із серії «Мистецтво» та
1 марку із серії «Звірі» вона подарувала подружці. 
Скільки марок лишилось у Оксани?
"""
stamps_art = 20
stamps_animals = 7
gift_art = 5
gift_animals = 1
art_left = stamps_art - gift_art
animals_left = stamps_animals - gift_animals
total_count_stamps_left = art_left + animals_left
print(f"Залишилось марок: {total_count_stamps_left}")


# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
apple_trees = 4
pear_trees = apple_trees + 5
plum_trees = apple_trees - 2
total_trees = apple_trees + pear_trees + plum_trees
print(f"General_count: {total_trees}")

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
temp_morning = 0 + 5
temp_afternoon = temp_morning - 10
temp_evening = temp_afternoon + 4
print(f"current temperature: {temp_evening}")


# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
boys_total = 24
girls_total = 24 / 2
boys_present = boys_total - 1
girls_present = girls_total - 2
present_children = boys_present + girls_present
print(f"total children present group today: {present_children}")

boys_total = 24
girls_total = 24 // 2
boys_present = boys_total - 1
girls_present = girls_total - 2
present_children = boys_present + girls_present
print(f"total children present group today: {present_children}")



# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""

first_book = 8
second_book = first_book + 2
third_book = (first_book + second_book) // 2
total_cost_book = first_book + second_book + third_book
print(f"Total cost if you buy one copy of each book: {total_cost_book}")