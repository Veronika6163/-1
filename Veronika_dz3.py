" Задача 1.Розробіть скрипт, який відкриває існуючий текстовий файл, зчитує його вміст та виводить його на екран. "
# task 1
def read_entire_file(path_file):
    text_file = open(path_file, 'r', encoding='utf-8')
    content = text_file.read()
    print(content)
    text_file.close()

read_entire_file("example.txt")

" Задача 2.Створіть програму, яка переіменовує файл з одного імені в інше. rename_file(path_to_file, new_name) "
# task 2
import os

def rename_file(path_to_file, new_name):
    os.rename(path_to_file, new_name)

rename_file("old_file.txt", "renamed_file.txt")

" Задача 3.Напишіть скрипт для копіювання вмісту одного текстового файлу в інший. copy_to_file(source_file, new_file) "
# task 3
def copy_to_file(source_file, new_file):
    file_to_read = open(source_file, 'r', encoding='utf-8')
    content = file_to_read.read()
    file_to_read.close()

    file_to_write = open(new_file, 'w', encoding='utf-8')
    file_to_write.write(content)
    file_to_write.close()


copy_to_file("source.txt", "copied_file.txt")

" Задача 4.Розробіть програму, яка визначає кількість слів у текстовому файлі. count_words(path_to_file) "
# task 4
def count_words(path_to_file):
    text_file = open(path_to_file, 'r', encoding='utf-8')
    content = text_file.read()
    text_file.close()

    words_list = content.split()

    words_count = len(words_list)

    print(words_count)


count_words("text_for_counting.txt")

" Задача 5.Створіть скрипт, який видаляє текстовий файл. remove_file(path_file). Повертає помилку якщо файла не існує/ "
# task 5
import os

def remove_file(path_file):
    if os.path.exists(path_file):
        os.remove(path_file)
    else:
        print("Помилка: файла не існує")

remove_file("file_to_delete.txt")

" Задача 6.Напишіть програму, яка додає новий рядок до існуючого текстового файлу add_data_to_file(path_file , text)."
# task 6
def add_data_to_file(path_file, text):
    text_file = open(path_file, 'a', encoding='utf-8')
    text_file.write("\n" + text)
    text_file.close()

add_data_to_file("existing_file.txt", "Це новий рядок.")

" Задача 7.Розробіть скрипт, який перевіряє наявність файлу за заданим ім'ям та повідомляє користувача про результат. функція має повертати True/False."
# task 7
import os

def check_file_exists(file_name):
    if os.path.exists(file_name):
        print("Повідомлення: такий файл існує!")
        return True
    else:
        print("Повідомлення: такого файлу не знайдено.")
        return False

check_file_exists("fake_file.txt")
check_file_exists("existing_file.txt")

" Задача 8.Створіть програму, яка шукає вказаний текст у файлі та виводить номери рядків, де цей текст знаходиться find_text(path_file, search_text )"
# task 8
def find_text(path_file, search_text):
    text_file = open(path_file, 'r', encoding='utf-8')
    lines = text_file.readlines()
    text_file.close()

    line_number = 1
    for line in lines:
        if search_text in line:
            print(line_number)
        line_number += 1

find_text("search_file.txt", "Яблуко")

" Задача 9.Напишіть скрипт, який сортує вміст текстового файлу за алфавітом і зберігає відсортований результат у новому файлі. sort_data_in_file(file_path). Результатом має бути новий файл з наступною назвою {file_path}_sorted"
# task 9
def sort_data_in_file(file_path):
    text_file = open(file_path, 'r', encoding='utf-8')
    lines = text_file.readlines()
    text_file.close()

    lines.sort()

    new_file_name = file_path + "_sorted"
    new_file = open(new_file_name, 'w', encoding='utf-8')
    for line in lines:
        new_file.write(line)
    new_file.close()

sort_data_in_file("data.txt")

" Задача 10.Розробіть функцію, яка перевіряє розмір файлу і повідомляє користувача, чи він перевищує заданий ліміт. is_greater_size(file_path, limit)"
# task 10
import os

def is_greater_size(file_path, limit):
    file_size = os.path.getsize(file_path)

    if file_size > limit:
        print("Повідомлення: розмір файлу перевищує ліміт.")
    else:
        print("Повідомлення: розмір файлу в межах ліміту.")


is_greater_size("data.txt", 10)
is_greater_size("data.txt", 10000)

" Задача 11.Напишіть скрипт для копіювання усіх файлів з одного каталогу в інший. copy_folder(from_folder , to_folder)"
# task 11
import os
import shutil

def copy_folder(from_folder, to_folder):
    if not os.path.exists(from_folder):
        print("Помилка: вихідної папки не існує.")
        return

    if not os.path.exists(to_folder):
        os.makedirs(to_folder)

    for item_name in os.listdir(from_folder):
        source_path = os.path.join(from_folder, item_name)
        destination_path = os.path.join(to_folder, item_name)

        if os.path.isfile(source_path):
            shutil.copy(source_path, destination_path)

    print("Усі файли успішно скопійовано!")

copy_folder("my_source_folder", "my_dest_folder")

" Задача 12.Створіть функцію, яка читає CSV-файл і виводить на екран лише певні стовпці."
# task 12
import csv

file_to_write = open("students.csv", "w", encoding="utf-8")
file_to_write.write("Прізвище,Оцінка\n")
file_to_write.write("Іванов,5\n")
file_to_write.write("Петров,4\n")
file_to_write.close()

def read_csv_columns(file_path, columns_to_print):
    file = open(file_path, 'r', encoding='utf-8')
    reader = csv.reader(file)

    headers = next(reader)

    indices = []
    for col_name in columns_to_print:
        if col_name in headers:
            indices.append(headers.index(col_name))

    for row in reader:
        for i in indices:
            print(row[i], end=" ")
        print()

    file.close()

read_csv_columns("students.csv", ["Прізвище", "Оцінка"])

"Задача 13.Напишіть скрипт, який створює архів з кількох файлів та розпаковує його. має бути дві функціїcreate_archive (*files) unpacking_archive(path_to_archive)"
# task 13
import zipfile

def create_archive(*files):
    archive_name = "my_files.zip"
    zip_container = zipfile.ZipFile(archive_name, 'w')

    for file_name in files:
        zip_container.write(file_name)

    zip_container.close()
    print("Архів створено успішно")
    return archive_name


def unpacking_archive(path_to_archive):
    zip_container = zipfile.ZipFile(path_to_archive, 'r')
    zip_container.extractall("unpacked_data")
    zip_container.close()
    print("Архів розпаковано успішно")


first_file = open("doc1.txt", "w")
first_file.write("Це перший тестовий файл")
first_file.close()

second_file = open("doc2.txt", "w")
second_file.write("Це другий тестовий файл")
second_file.close()

create_archive("doc1.txt", "doc2.txt")
unpacking_archive("my_files.zip")

" Задача 14.Розробіть функцію, яка змінює права доступу до файлу (наприклад, робить його доступним лише для читання або запису)."
# task 14
import os
import stat

def change_file_permissions(file_path):
    new_file = open(file_path, "w")
    new_file.write("Цей файл зараз стане доступним тільки для читання.")
    new_file.close()

    print("Файл успішно створено.")

    os.chmod(file_path, stat.S_IREAD)

    print("Права доступу змінено: тепер файл тільки для читання.")


change_file_permissions("test_permissions.txt")


" Задача 15.Створіть функцію, яка виводить список всіх файлів у заданому каталозі та його підкаталогах."
# task 15
import os

def list_all_files(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            full_path = os.path.join(root, file_name)
            print(full_path)

current_directory = os.getcwd()
list_all_files(current_directory)

" Задача 16.Напишіть функцію, яка масово перейменовує файли у заданому каталозі за певним шаблоном. Додайте до кожної назви файла префікс rename_"
# task 16
import os

def rename_files(directory_path):
    all_items = os.listdir(directory_path)

    for item_name in all_items:
        old_full_path = os.path.join(directory_path, item_name)

        if os.path.isfile(old_full_path):
            new_name = "rename_" + item_name
            new_full_path = os.path.join(directory_path, new_name)

            os.rename(old_full_path, new_full_path)


folder_name = "test_rename_folder"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)

first_file = open(os.path.join(folder_name, "test1.txt"), "w")
first_file.write("Текст для першого файлу")
first_file.close()

second_file = open(os.path.join(folder_name, "test2.txt"), "w")
second_file.write("Текст для другого файлу")
second_file.close()

rename_files(folder_name)

" Задача 17.Створіть скрипт, який зчитує XML-файл та витягує з нього певну інформацію."
# task 17
xml_file = open("company_data.xml", "w", encoding="utf-8")
xml_file.write("<company>\n")
xml_file.write("    <employee>\n")
xml_file.write("        <name>Олена</name>\n")
xml_file.write("        <position>Менеджер</position>\n")
xml_file.write("    </employee>\n")
xml_file.write("    <employee>\n")
xml_file.write("        <name>Іван</name>\n")
xml_file.write("        <position>Програміст</position>\n")
xml_file.write("    </employee>\n")
xml_file.write("</company>\n")
xml_file.close()

text_file = open("company_data.xml", "r", encoding="utf-8")

for line in text_file:
    if "<name>" in line:
        clean_name = line.replace("<name>", "")
        clean_name = clean_name.replace("</name>", "")
        clean_name = clean_name.strip()
        print(clean_name)

text_file.close()

" Задача 18.Розробіть скрипт, який переформатовує CSV-файл, видаляючи дублікати рядків та зберігаючи результат у новому файлі."
# task 18
test_csv = open("data.csv", "w", encoding="utf-8")
test_csv.write("Ім'я,Вік,Посада\n")
test_csv.write("Олена,25,Менеджер\n")
test_csv.write("Іван,30,Програміст\n")
test_csv.write("Олена,25,Менеджер\n")
test_csv.write("Марія,28,Дизайнер\n")
test_csv.write("Іван,30,Програміст\n")
test_csv.close()

source_file = open("data.csv", "r", encoding="utf-8")
result_file = open("cleaned_data.csv", "w", encoding="utf-8")

seen_rows = set()

for row in source_file:
    if row not in seen_rows:
        result_file.write(row)
        seen_rows.add(row)

source_file.close()
result_file.close()

print("Дублікати успішно видалено!")

" Задача 19.Створіть функцію для пошуку файлів з певним розширенням у вказаному каталозі та всіх його підкаталогах."
# task 19
import os

def find_files_by_extension(directory_path, extension):
    found_files = []

    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            if file_name.endswith(extension):
                full_path = os.path.join(root, file_name)
                found_files.append(full_path)

    return found_files

test_folder = "search_test_folder"

if not os.path.exists(test_folder):
    os.mkdir(test_folder)

file1 = open(os.path.join(test_folder, "report.txt"), "w")
file1.write("Звіт")
file1.close()

file2 = open(os.path.join(test_folder, "photo.jpg"), "w")
file2.write("Фото")
file2.close()

file3 = open(os.path.join(test_folder, "notes.txt"), "w")
file3.write("Нотатки")
file3.close()

result_list = find_files_by_extension(test_folder, ".txt")

for file_path in result_list:
    print(file_path)

" Задача 20.Створіть функцію для створення текстового файлу, в якому кожний рядок містить назву файлу, його розмір та дату створення, для всіх файлів у вказаному каталозі."
# task 20
import os
import time

def write_file_info(directory_path, output_filename):
    result_file = open(output_filename, "w", encoding="utf-8")
    all_items = os.listdir(directory_path)

    for item_name in all_items:
        full_path = os.path.join(directory_path, item_name)

        if os.path.isfile(full_path):
            file_size = os.path.getsize(full_path)
            raw_time = os.path.getctime(full_path)
            readable_time = time.ctime(raw_time)

            line_to_write = "Назва: " + item_name + ", Розмір: " + str(
                file_size) + " байт, Дата: " + readable_time + "\n"
            result_file.write(line_to_write)

    result_file.close()


test_folder = "info_test_folder"

if not os.path.exists(test_folder):
    os.mkdir(test_folder)

file1 = open(os.path.join(test_folder, "document.txt"), "w")
file1.write("Текст документа")
file1.close()

file2 = open(os.path.join(test_folder, "picture.png"), "w")
file2.write("Імітація картинки")
file2.close()

write_file_info(test_folder, "files_info.txt")

"Задача 21.Розробіть функцію для знаходження найбільшого та найменшого файлів у вказаному каталозі."
# task 21
import os

def find_largest_and_smallest(directory_path):
    largest_file = ""
    smallest_file = ""
    max_size = -1
    min_size = -1

    all_items = os.listdir(directory_path)

    for item_name in all_items:
        full_path = os.path.join(directory_path, item_name)

        if os.path.isfile(full_path):
            current_size = os.path.getsize(full_path)

            if max_size == -1 or current_size > max_size:
                max_size = current_size
                largest_file = item_name

            if min_size == -1 or current_size < min_size:
                min_size = current_size
                smallest_file = item_name

    print("Найбільший файл:", largest_file, "Розмір:", max_size)
    print("Найменший файл:", smallest_file, "Розмір:", min_size)

test_dir = "size_test_folder"

if not os.path.exists(test_dir):
    os.mkdir(test_dir)

file_small = open(os.path.join(test_dir, "small.txt"), "w")
file_small.write("А")
file_small.close()

file_large = open(os.path.join(test_dir, "large.txt"), "w")
file_large.write("Тут багато тексту, щоб цей файл став найбільшим у цій папці.")
file_large.close()

find_largest_and_smallest(test_dir)

" Задача 22.Створіть функцію для об'єднання вмісту декількох текстових файлів у один файл."
# task 22
def merge_text_files(file_list, output_filename):
    result_file = open(output_filename, "w", encoding="utf-8")

    for file_name in file_list:
        source_file = open(file_name, "r", encoding="utf-8")
        content = source_file.read()

        result_file.write(content)
        result_file.write("\n")

        source_file.close()

    result_file.close()

file1 = open("part1.txt", "w", encoding="utf-8")
file1.write("Це текст із першого файлу.")
file1.close()

file2 = open("part2.txt", "w", encoding="utf-8")
file2.write("А це текст із другого файлу, який ми додамо в кінець.")
file2.close()

my_files = ["part1.txt", "part2.txt"]
merge_text_files(my_files, "merged_result.txt")

print("Файли успішно об'єднано!")

" Задача 23.Створіть функцію, яка перевіряє, чи усі файли у вказаному каталозі мають однаковий розмір."
# task 23
import os

def are_files_equal_size(directory_path):
    reference_size = -1

    all_items = os.listdir(directory_path)

    for item_name in all_items:
        full_path = os.path.join(directory_path, item_name)

        if os.path.isfile(full_path):
            current_size = os.path.getsize(full_path)

            if reference_size == -1:
                reference_size = current_size
            else:
                if current_size != reference_size:
                    return False

    return True

test_directory = "equal_size_test_folder"

if not os.path.exists(test_directory):
    os.mkdir(test_directory)

first_file = open(os.path.join(test_directory, "first_file.txt"), "w")
first_file.write("Hello")
first_file.close()

second_file = open(os.path.join(test_directory, "second_file.txt"), "w")
second_file.write("World")
second_file.close()

result = are_files_equal_size(test_directory)
print("Чи всі файли однакового розміру?", result)

" Задача 24.Розробіть скрипт для вилучення всіх коментарів з файлу програмного коду на мові Python."
# task 24
def remove_comments_from_file(input_filename, output_filename):
    source_file = open(input_filename, "r", encoding="utf-8")
    result_file = open(output_filename, "w", encoding="utf-8")

    for line in source_file:
        line_without_spaces = line.strip()

        if not line_without_spaces.startswith("#"):
            result_file.write(line)

    source_file.close()
    result_file.close()

test_input_file = open("test_script.py", "w", encoding="utf-8")
test_input_file.write("print('Початок програми')\n")
test_input_file.write("# Це коментар, його треба видалити\n")
test_input_file.write("x = 10\n")
test_input_file.write("    # Це коментар з відступом, його теж видаляємо\n")
test_input_file.write("print(x)\n")
test_input_file.close()

remove_comments_from_file("test_script.py", "clean_script.py")

print("Коментарі успішно видалено!")

" Задача 25.Створіть скрипт, який автоматично видаляє файли, які не змінювалися протягом останнього місяця, з вказаного каталогу"
# task 25
import os
import time

def delete_old_files(directory_path):
    current_time = time.time()
    one_month_in_seconds = 30 * 24 * 60 * 60

    all_items = os.listdir(directory_path)

    for item_name in all_items:
        full_path = os.path.join(directory_path, item_name)

        if os.path.isfile(full_path):
            modification_time = os.path.getmtime(full_path)
            time_difference = current_time - modification_time

            if time_difference > one_month_in_seconds:
                os.remove(full_path)
                print("Видалено старий файл:", item_name)

test_directory = "delete_test_folder"

if not os.path.exists(test_directory):
    os.mkdir(test_directory)

recent_file = open(os.path.join(test_directory, "fresh_file.txt"), "w")
recent_file.write("Цей файл створено щойно.")
recent_file.close()

old_file_path = os.path.join(test_directory, "old_file.txt")
old_file = open(old_file_path, "w")
old_file.write("Цей файл буде виглядати так, ніби йому 40 днів.")
old_file.close()

forty_days_in_seconds = 40 * 24 * 60 * 60
past_time = time.time() - forty_days_in_seconds
os.utime(old_file_path, (past_time, past_time))

delete_old_files(test_directory)

" Задача 26.Напишіть функцію для розділу списку на два підсписки, використовуючи певний елемент як роздільник. Врахуйте можливі помилки, такі як відсутність роздільника чи невірний тип даних у списку."
# task 26
def split_list_by_element(input_list, separator):
    if not isinstance(input_list, list):
        return "Помилка: Перший аргумент має бути списком"

    found_separator = False
    for item in input_list:
        if item == separator:
            found_separator = True
            break

    if found_separator == False:
        return "Помилка: Роздільник не знайдено у списку"

    first_part = []
    second_part = []
    reached_separator = False

    for item in input_list:
        if item == separator and reached_separator == False:
            reached_separator = True
            continue

        if reached_separator == False:
            first_part.append(item)
        else:
            second_part.append(item)

    return first_part, second_part

my_list = [10, 20, 30, "separator", 40, 50]
my_separator = "separator"

result = split_list_by_element(my_list, my_separator)

if isinstance(result, tuple):
    first_half, second_half = result
    print("Перша частина:", first_half)
    print("Друга частина:", second_half)
else:
    print(result)

" Задача 27.Розробіть функцію для обчислення податку на прибуток за різними ставками. Використовуйте try-except, щоб обробити можливі помилки введення користувача або некоректні дані."
# task 27
def calculate_income_tax(annual_income):
    try:
        income_value = float(annual_income)

        if income_value < 0:
            return "Помилка: Дохід не може бути від'ємним"

        if income_value <= 10000:
            tax_rate = 0.05
        elif income_value <= 50000:
            tax_rate = 0.10
        else:
            tax_rate = 0.18

        total_tax = income_value * tax_rate
        return total_tax

    except ValueError:
        return "Помилка: Введено нечислове значення"
    except Exception:
        return "Помилка: Виникла непередбачувана помилка при обчисленні"

user_input = "55000"
result = calculate_income_tax(user_input)

if isinstance(result, float):
    print("Сума податку складає:", result)
else:
    print(result)

invalid_input = "п'ятсот гривень"
print("Перевірка на текст:", calculate_income_tax(invalid_input))

negative_input = "-100"
print("Перевірка на від'ємне число:", calculate_income_tax(negative_input))

" Задача 28.Створіть програму для валідації електронної адреси користувача. Використовуйте try-except, щоб обробити помилки формату або відсутності необхідних компонентів (наприклад, "@")."
# task 28
def validate_email_address(user_email):
    try:
        if not isinstance(user_email, str):
            raise ValueError("Введені дані не є рядком")

        if "@" not in user_email:
            raise ValueError("Відсутній символ '@'")

        parts_of_email = user_email.split("@")

        if len(parts_of_email) != 2:
            raise ValueError("Адреса повинна містити рівно один символ '@'")

        username_part = parts_of_email[0]
        domain_part = parts_of_email[1]

        if len(username_part) == 0:
            raise ValueError("Ім'я користувача перед '@' не може бути порожнім")

        if "." not in domain_part:
            raise ValueError("Доменна частина після '@' повинна містити крапку")

        return True

    except ValueError as error_message:
        return f"Помилка валідації: {error_message}"

test_email = "veronika@example.com"
result = validate_email_address(test_email)

if result == True:
    print("Електронна адреса", test_email, "є коректною.")
else:
    print(result)

print(validate_email_address("myemail.com"))

print(validate_email_address("@example.com"))

print(validate_email_address(12345))

" Задача 29.Напишіть код, який зчитує вміст HTML-файлу та виводить список всіх URL-адрес у файлі."
# task 29
# task 29
def extract_urls_from_html(file_name):
    try:
        html_file = open(file_name, "r", encoding="utf-8")
        content = html_file.read()
        html_file.close()

        urls_list = []
        search_position = 0

        while True:
            start_index = content.find('href="', search_position)

            if start_index == -1:
                break

            start_index = start_index + 6
            end_index = content.find('"', start_index)

            if end_index == -1:
                break

            url_address = content[start_index:end_index]

            if url_address not in urls_list:
                urls_list.append(url_address)

            search_position = end_index

        return urls_list

    except FileNotFoundError:
        return "Помилка: Файл не знайдено"

test_file = open("example.html", "w", encoding="utf-8")
test_file.write('<html><body>\n')
test_file.write('<a href="https://pythonguide.rozh2sch.org.ua">Довідник Python</a>\n')
test_file.write('<a href="https://acode.com.ua/lessons-python/">Уроки Python</a>\n')
test_file.write(
    '<a href="https://sites.google.com/comp-sc.if.ua/python-easy/%D0%B4%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D1%8F-%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B0?authuser=0">Python Easy</a>\n')
test_file.write('</body></html>')
test_file.close()

found_urls = extract_urls_from_html("example.html")

if isinstance(found_urls, list):
    print("Список знайдених адрес:")
    for url in found_urls:
        print(url)
else:
    print(found_urls)