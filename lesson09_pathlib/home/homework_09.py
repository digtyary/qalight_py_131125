### Робота з файлами та папками — завдання
"""
1. **Створення файлу**
   Створи текстовий файл `hello.txt` і запиши в нього рядок:

   ```
   Hello, Python!
   ```
"""
from pathlib import Path

# coding here
file_hello = Path("hello.txt")
file_hello.write_text("Hello, Python!\n" , encoding= "utf-8")
"""
2. **Читання файлу**
   Відкрий файл `hello.txt` і виведи його вміст на екран.
"""
# coding here
content = file_hello.read_text(encoding= "utf-8")
print(content)
"""   
3. **Дозапис у файл**
   Додай у файл `hello.txt` ще один рядок:

   ```
   Learning file operations.
   ```
"""
# coding here
with file_hello.open("a") as f:
    f.write("Learning file operations.\n")

"""
4. **Читання кількох рядків**
   Виведи всі рядки з файлу `hello.txt` по одному рядку (без додаткових символів `\n`).
"""
# coding here
with file_hello.open("r" , encoding="utf-8") as f:
    for line in f:
        print(line.strip())
"""
5. **Підрахунок символів**
   Прочитай файл `hello.txt` і виведи кількість символів у ньому.
"""
# coding here
text = file_hello.read_text(encoding= "utf-8")
print(len(text))
"""
6. **Створення папки**
   Створи папку з назвою `data`. Усередині неї створи файл `notes.txt` із текстом:

   ```
   My first note.
   ```
"""
# coding here
data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

note_file = data_dir / "notes.txt"
note_file.write_text("My first note.", encoding="utf-8")
"""
7. **Список файлів у папці**
   Виведи на екран список усіх файлів у папці `data`.
"""
# coding here
for item in data_dir.iterdir():
    if item.is_file():
        print(item.name)

"""
8. **Копіювання вмісту**
   Прочитай вміст файлу `notes.txt` і запиши його у файл `copy.txt` (у тій же папці `data`).
"""
# coding here
copy_file = data_dir / "copy.txt"

notes_content = note_file.read_text(encoding= "utf-8")
copy_file.write_text(notes_content , encoding= "utf-8")
"""
9. **Об’єднання файлів**
   Створи два файли: `a.txt` і `b.txt`, кожен із будь-яким текстом.
   Запиши їхній вміст у новий файл `ab.txt`.
"""
# coding here
a_file = Path("a.txt")
b_file = Path("b.txt")
ab_file = Path("ab.txt")

a_file.write_text("A\n", encoding="utf-8")
b_file.write_text("B\n", encoding="utf-8")

combined = (a_file.read_text(encoding="utf-8") + b_file.read_text(encoding="utf-8"))
ab_file.write_text(combined, encoding="utf-8")

"""
10. **Пошук слова у файлі**
    У файлі `notes.txt` перевір, чи є слово `"note"`.
    Якщо є — виведи `"Знайдено"`, інакше `"Не знайдено"`.
"""
# coding here
notes_text = note_file.read_text(encoding= "utf-8")

if "note" in notes_text:
    print("Знайдено")
else:
    print("Не знайдено")
