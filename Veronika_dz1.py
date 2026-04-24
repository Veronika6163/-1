" Задача 1.Дані два цілих числа. Виведіть значення найменшого."
# task 1
print("Enter first number:")
number1 = int(input())
print("Enter second number:")
number2 = int(input())

if number1 < number2:
    print("The smallest number is: " + str(number1))
else:
    print("The smallest number is: " + str(number2))

"Задача 2.Задано дві клітинки шахівниці. Якщо вони пофарбовані в один колір, виведіть слово YES, а якщо в різні кольори - то NO. Програма отримує на вхід чотири числа від 1 до 8 кожне, що задають номер стовпця та номер рядка спочатку для першої клітини, потім для другої клітини."
# task 2
print("Enter coordinates for two cells (4 numbers from 1 to 8):")
column1 = int(input())
row1 = int(input())
column2 = int(input())
row2 = int(input())

if (column1 + row1) % 2 == (column2 + row2) % 2:
    print("YES")
else:
    print("NO")

""" задача 3.Якщо вводиться температура в градусах за шкалою Цельсія, вона переводиться в температуру за шкалою Фаренгейта. Або навпаки: температура за Фаренгейтом переводиться в температуру за Цельсієм. """
# task 3
print("What do you want to convert?")
print("1 - Celsius to Fahrenheit")
print("2 - Fahrenheit to Celsius")
choice = input("Enter 1 or 2: ").strip()

if choice == '1':
    celsius_input = float(input("Enter temperature in Celsius: "))
    fahrenheit_output = (celsius_input * 9 / 5) + 32
    print("Temperature in Fahrenheit: " + str(fahrenheit_output))
elif choice == '2':
    fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))
    celsius_output = (fahrenheit_input - 32) * 5 / 9
    print("Temperature in Celsius: " + str(celsius_output))
else:
    print("Invalid input. Please enter 1 or 2.")

"задача 4 Зі списку випадкових чисел,визначити та вивести на екран непарні числа."
# task 4
import random

random_numbers_list = []

for iteration in range(10):
    generated_value = random.randint(1, 100)
    random_numbers_list.append(generated_value)

print("Full list of generated numbers:")
print(random_numbers_list)

print("Only odd numbers from the list:")
for current_number in random_numbers_list:

    if current_number % 2 != 0:
        print(current_number)

""" задача 5.Вводиться ціле число, що означає код символу за таблицею ASCII. Визначити, це код англійської літери або будь-який інший символ.  """
# task 5
user_input = input("Enter any single character: ")
if 'a' <= user_input <= 'z' or 'A' <= user_input <= 'Z':
    print("This is an English letter")
else:
    print("This is not an English letter")

" задача 6. Вводяться два цілих числа. Перевірити чи ділиться перше на друге. Вивести на екран повідомлення про це, а також залишок (якщо він є) та приватне (у будь-якому випадку)."
# task 6
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

quotient = first_number // second_number
remainder = first_number % second_number

print("Quotient:", quotient)
print("Remainder:", remainder)

if remainder == 0:
    print("The first number is divisible by the second.")
else:
    print("The first number is not divisible by the second.")

""" задача 7.По черзі вводиться 5 цифр, вивести їхню суму (скориставшись for)  """
# task 7
total_sum = 0

print("Please enter 5 numbers one by one:")

for iteration in range(5):
    current_number = int(input("Enter a number: "))

    total_sum = total_sum + current_number

print("The total sum of the entered numbers is:")
print(total_sum)

"""задача 8.Дано два цілих числа A і B. Виведіть усі числа від A до B включно, в порядку зростання, якщо A < B, або в порядку убування інакше."""
# task 8
first_number = int(input("Enter number A: "))
second_number = int(input("Enter number B: "))

if first_number < second_number:
    print("Increasing order:")

    for current_number in range(first_number, second_number + 1):
        print(current_number)
else:
    print("Decreasing order:")

    for current_number in range(first_number, second_number - 1, -1):
        print(current_number)

""" задача 9.Циклом for вивести ромб"""
# task 9
size = 5

for row in range(1, size + 1):
    print(" " * (size - row), end="")

    print("*" * (2 * row - 1))

for row in range(size - 1, 0, -1):
    print(" " * (size - row), end="")

    print("*" * (2 * row - 1))


"""задача 10.Порахувати суму числового ряду від 0 до 14 включно. Наприклад, 0+1+2+3+…+14;"""
# task 10
total_sum = 0

for current_number in range(15):
    total_sum = total_sum + current_number

print("The sum of numbers from 0 to 14 is:")
print(total_sum)

""" задача 11.Перемножити всі парні значення в діапазоні від 0 до 436"""
# task 11
product = 1

for even_number in range(2, 437, 2):
    product = product * even_number

print("The product of all even numbers from 2 to 436 is:")
print(product)

"""задача 12.Задається випадкове речове число. Визначте максимальну цифру цього числа. Приклад виконання: 56.457 -> 7"""
# task 12
import random

random_number = random.uniform(1, 100)

random_number = round(random_number, 3)
print(f"Generated random number: {random_number}")

if random_number < 0:
    random_number = -random_number

while random_number % 1 != 0:
    random_number = round(random_number * 10, 10)

number_as_integer = int(random_number)
maximum_digit = 0

while number_as_integer > 0:

    current_digit = number_as_integer % 10

    if current_digit > maximum_digit:
        maximum_digit = current_digit

    number_as_integer = number_as_integer // 10

print("The maximum digit in the number is:", maximum_digit)

"""задача 13.Факторіалом числа n називається число 𝑛! = 1∙2∙3∙…∙𝑛. Створіть програму, яка обчислює фактор введеного користувачем числа. (Цикл!)"""
# task 13
user_number = int(input("Enter an integer to calculate its factorial: "))

factorial_result = 1
current_multiplier = 1

while current_multiplier <= user_number:
    factorial_result = factorial_result * current_multiplier
    current_multiplier = current_multiplier + 1

print(f"The factorial of {user_number} is: {factorial_result}")

"""задача 14.Використовуючи вкладені цикли та функції print('*', end=''), print(' ', end='') та print() виведіть на екран прямокутний трикутник."""
# task 14
triangle_height = int(input("Enter the height of the triangle: "))

for current_row in range(1, triangle_height + 1):

    for space_index in range(triangle_height - current_row):
        print(' ', end='')

    for star_index in range(current_row):
        print('*', end='')

    print()

"""задача 15.Користувач робить внесок у розмірі N $ строком на роки під 11.5% річних (кожний рік розмір його вкладу збільшується на 11,5%. Ці гроші додаються до суми вкладу, і на них наступного року також будуть відсотки). Написати програму , де користувач вводить аргументи a та years, і порахувати суму, яка буде на рахунку користувача через роки."""
# task 15
deposit_amount = float(input("Enter the initial deposit amount: "))
deposit_years = int(input("Enter the number of years: "))

for current_year in range(deposit_years):

    deposit_amount = deposit_amount + (deposit_amount * 0.115)

deposit_amount = int(deposit_amount * 100) / 100

print("The amount on the account after", deposit_years, "years will be:")
print(deposit_amount)

"""задача 16.Користувач вводить рік. Визначити він високосний чи ні."""
# task 16
input_year = int(input("Enter a year to check: "))

if input_year % 400 == 0 or (input_year % 4 == 0 and input_year % 100 != 0):
    print("This is a leap year.")
else:
    print("This is not a leap year.")

"""задача 17.Напишіть програму, яка запитує три цілі числа a, b і x і виводить True, якщо x лежить між a і b, інакше - False.."""
# task 17
first_boundary = int(input("Enter the first boundary (a): "))
second_boundary = int(input("Enter the second boundary (b): "))
target_number = int(input("Enter the number to check (x): "))

if first_boundary <= target_number <= second_boundary or second_boundary <= target_number <= first_boundary:
    print(True)
else:
    print(False)

"""задача 18.Дано чотири дійсні числа: x1, y1, x2, y2. обчисліть відстань між точкою (x1, y1) та (x2, y2). Вважайте чотири дійсні числа та виведіть результат роботи цієї функції."""
# task 18
def calculate_distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

x1 = float(input("Enter coordinate x1: "))
y1 = float(input("Enter coordinate y1: "))
x2 = float(input("Enter coordinate x2: "))
y2 = float(input("Enter coordinate y2: "))

distance_result = calculate_distance(x1, y1, x2, y2)
print("The distance between the points is:", distance_result)

"""задача 19.Запитайте користувача про число n. Знайдіть суму всіх чисел від 1 до n."""
# task 19
target_number = int(input("Enter an integer: "))

total_sum = 0

for current_number in range(1, target_number + 1):
    total_sum += current_number

print("The sum of all numbers from 1 to", target_number, "is:", total_sum)

"""задача 20.Виведіть таблицю множення для числа, яке вводить користувач (наприклад, таблицю множення для 5)."""
# task 20
target_number = int(input("Enter a number for the multiplication table: "))

print("Multiplication table for number", target_number, ":")

for multiplier in range(1, 11):

    current_result = target_number * multiplier

    print(target_number, "x", multiplier, "=", current_result)

"""задача 21.Перевірте, чи є введене число простим. Виведіть повідомлення про результат."""
# task 21
number = int(input("Enter an integer to check: "))

if number <= 1:
    print(number, "is not prime.")
else:
    is_prime = True

    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break

    if is_prime == True:
        print(number, "is a prime number!")
    else:
        print(number, "is not a prime number.")

"""задача 22.Згенеруйте випадкове число в заданому діапазоні. Дайте користувачу спробу вгадати це число. Виведіть повідомлення про результат."""
# task 22
import random

secret_number = random.randint(1, 100)

user_guess = int(input("I guessed a number from 1 to 100. Try to guess it: "))

if user_guess == secret_number:
    print("Congratulations! You guessed it!")
else:
    print("You didn't guess. It was the number", secret_number)

"""задача 23.Перевірте, чи є це слово паліндромом (читається однаково зліва направо і справа наліво)."""

# task 23
user_word = input("Enter a word to check: ")

lowercase_word = user_word.lower()

reversed_word = ""

for letter in lowercase_word:
    reversed_word = letter + reversed_word

if lowercase_word == reversed_word:
    print("This word is a palindrome!")
else:
    print("This word is NOT a palindrome.")

"""задача 24.Відсортуйте цей список за допомогою алгоритму сортування бульбашкою."""
# task 24
numbers = [64, 34, 25, 12, 22, 11, 90]
print("List before sorting:", numbers)

list_length = len(numbers)

for current_pass in range(list_length - 1):

    for index in range(list_length - 1 - current_pass):

        if numbers[index] > numbers[index + 1]:
            temporary_value = numbers[index]
            numbers[index] = numbers[index + 1]
            numbers[index + 1] = temporary_value

print("List after sorting:", numbers)

"""задача 25.Створіть список чисел в діапазоні від 1 до n, пропустивши одне число. Знайдіть та виведіть пропущене число. наприклад some_list =[1,2,3,5,6,7] , пропущене число - 4."""
# task 25
limit = 7
numbers_list = [1, 2, 3, 5, 6, 7]

print("Original list:", numbers_list)

for expected_number in range(1, limit + 1):

    if expected_number not in numbers_list:
        print("The missing number is:", expected_number)

    """задача 26.Сіракузська послідовність Запитайте користувача про початкове число. Виведіть послідовність чисел за правилом: якщо число парне, поділіть його на 2, інакше помножте на 3 і додайте 1. Повторюйте цей процес, поки не досягнете числа 1."""
    # task 26
    current_number = int(input("Enter a starting number: "))

    print("Syracuse sequence:")

    print(current_number)

    while current_number != 1:

        if current_number % 2 == 0:

            current_number = current_number // 2
        else:

            current_number = current_number * 3 + 1

        print(current_number)

"""задача 27,28 Запитайте користувача про верхню межу діапазону. Знайдіть всі прості числа у заданому діапазоні і виведіть їх."""
# task 27, 28
upper_limit = int(input("Enter the upper limit of the range: "))

print("Prime numbers in your range:")

for number in range(2, upper_limit + 1):

    divisors_count = 0

    for divisor in range(2, number):
        if number % divisor == 0:
            divisors_count = divisors_count + 1
            break
    if divisors_count == 0:
        print(number, end=" ")

print()

"""задача 29 Переведення числа в текст Запитайте користувача про ціле число від 1 до 999. Виведіть це число прописом (наприклад, 123 → "сто двадцять три")."""
# task 29
number = int(input("Enter a number from 1 to 999: "))

hundreds_digit = number // 100
tens_digit = (number % 100) // 10
units_digit = number % 10

hundreds_words = ["", "сто", "двісті", "триста", "чотириста", "п'ятсот", "шістсот", "сімсот", "вісімсот", "дев'ятсот"]
tens_words = ["", "", "двадцять", "тридцять", "сорок", "п'ятдесят", "шістдесят", "сімдесят", "вісімдесят", "дев'яносто"]
units_words = ["", "один", "два", "три", "чотири", "п'ять", "шість", "сім", "вісім", "дев'ять"]

if hundreds_digit > 0:
    print(hundreds_words[hundreds_digit], end=" ")

if tens_digit == 1:
    if units_digit == 0:
        print("десять")
    elif units_digit == 1:
        print("одинадцять")
    elif units_digit == 2:
        print("дванадцять")
    elif units_digit == 3:
        print("тринадцять")
    elif units_digit == 4:
        print("чотирнадцять")
    elif units_digit == 5:
        print("п'ятнадцять")
    elif units_digit == 6:
        print("шістнадцять")
    elif units_digit == 7:
        print("сімнадцять")
    elif units_digit == 8:
        print("вісімнадцять")
    elif units_digit == 9:
        print("дев'ятнадцять")
else:

    if tens_digit > 1:
        print(tens_words[tens_digit], end=" ")

    if units_digit > 0:
        print(units_words[units_digit])

if number == 0:
    print("нуль")

"""задача 30 Створіть функцію для знаходження найменшого спільного кратного двох чисел."""
# task 30
def find_least_common_multiple(first_number, second_number):

    if first_number > second_number:
        current_multiple = first_number
    else:
        current_multiple = second_number

    while True:

        if (current_multiple % first_number == 0) and (current_multiple % second_number == 0):

            return current_multiple

        current_multiple = current_multiple + 1

input_number_one = int(input("Enter the first integer: "))
input_number_two = int(input("Enter the second integer: "))

final_result = find_least_common_multiple(input_number_one, input_number_two)

print("The least common multiple is:", final_result)




