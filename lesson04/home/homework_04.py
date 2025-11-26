adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while 
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

# УВАГА! Перезаписуйте вміст змінної adwentures_of_tom_sawer у завданнях 01-03

# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")


# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")


# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer.split())


# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
h_count = adwentures_of_tom_sawer.count("h")


# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
підказка - порахувати кожну велику літеру напр, .count("A") і їх сумму
"""
capital_count = 0
for word in adwentures_of_tom_sawer.split():
    if word[0].isalpha() and word[0].isupper():
        capital_count = capital_count + 1
print("Total words:", capital_count)



# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
first_pos = adwentures_of_tom_sawer.find("Tom")
second_pos = adwentures_of_tom_sawer.find("Tom", first_pos + 1)
print("second 'Tom' position:", second_pos)


# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = None

adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(". ")

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""

fourth_sentence_lower = adwentures_of_tom_sawer_sentences[3].lower()
print("Task8 — fourth sentence (lower):", fourth_sentence_lower)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
has_sentence = False
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.startswith("By the time"):
        has_sentence = True
print("Task9 — any sentence starts with 'By the time'?:", has_sentence)


# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
last_sentence = adwentures_of_tom_sawer_sentences[-1]
last_sentence_word_count = len(last_sentence.split())
print("Task10 — words in last sentence:", last_sentence_word_count)
