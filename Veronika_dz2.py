"""1)Напишіть функцію для визначення парності числа: is_even(7) - повертає false"""
# task 1
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
result = is_even(7)
print(result)
"""2)Напишіть функцію для обчислення факторіалу числа: factorial(4) - повертає 24"""
def factorial(number):
    result = 1

    for current_number in range(1, number + 1):
        result = result * current_number
    return result

print(factorial(4))

"""3)Напишіть функцію для виведення всіх парних чисел від 1 до n: print_even_numbers(10)"""
# task 3
def print_even_numbers(maximum_number):
    for current_number in range(1, maximum_number + 1):
        if current_number % 2 == 0:
            print(current_number)

print_even_numbers(10)

"""4)Напишіть функцію для переведення градусів Цельсія у градуси Фаренгейта celsius_to_fahrenheit(10)"""
# task 4
def celsius_to_fahrenheit(celsius):
    # Формула: (Цельсій * 9/5) + 32
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

result = celsius_to_fahrenheit(10)
print(result)

"""5)Напишіть функцію для обчислення площі прямокутника"""
# task 5
def calculate_rectangle_area(width, height):
    result = width * height
    return result

area = calculate_rectangle_area(5, 10)
print(f"Rectangle area: {area}")

"""6)Напишіть функцію для обчислення кількості голів та ніг у стаді худоби та курей count_animals(heads, legs)"""
# task 6
def count_animals(heads, legs):
    for cows in range(heads + 1):
        chickens = heads - cows

        if (cows * 4 + chickens * 2) == legs:
            return cows, chickens

animals_result = count_animals(10, 28)
print(f"Cows and chickens respectively: {animals_result}")

"""7)Напишіть функцію для перевірки простоти числа: is_prime(10)"""
# task 7
def is_prime(number):
    if number <= 1:
        return False

    for current_number in range(2, number):
        if number % current_number == 0:
            return False

    return True

print(is_prime(10))
print(is_prime(7))

"""8)Функція для перевірки паліндрому: is_palindrome('hello world')"""
# task 8
def is_palindrome(text):
    reversed_text = ""
    for letter in text:
        reversed_text = letter + reversed_text

    if text == reversed_text:
        return reversed_text
    else:
        return "Not a palindrome"

print(is_palindrome("radar"))
print(is_palindrome("hello"))

"""9)Функція для генерації списку простих чисел: generate_primes(30) (використайте функцію is_prime)"""
# task 9
def generate_prime_numbers(maximum_limit):
    list_of_primes = []

    for current_number in range(2, maximum_limit + 1):
        is_prime = True

        for possible_divisor in range(2, current_number):
            if current_number % possible_divisor == 0:
                is_prime = False
                break

        if is_prime == True:
            list_of_primes.append(current_number)

    return list_of_primes

print(generate_prime_numbers(30))

"""10)Функція для конвертації числа у римський запис: int_to_roman(100)"""
# task 10
def int_to_roman(number):

    roman_values = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]

    result = ""

    for value, symbol in roman_values:

        while number >= value:
            result = result + symbol
            number = number - value

    return result

print(int_to_roman(100))
print(int_to_roman(2026))
print(int_to_roman(4))

"""11)Функція для обчислення коренів квадратного рівняння: Функція для обчислення коренів квадратного рівняння:"""
# task 11
def solve_quadratic_equation(a, b, c):
    discriminant = (b ** 2) - (4 * a * c)

    if discriminant > 0:
        root1 = (-b + discriminant ** 0.5) / (2 * a)
        root2 = (-b - discriminant ** 0.5) / (2 * a)
        return root1, root2

    elif discriminant == 0:
        root = -b / (2 * a)
        return root

    else:
        return "No real roots"

print(solve_quadratic_equation(1, -3, 2))
print(solve_quadratic_equation(1, 2, 1))
print(solve_quadratic_equation(1, 0, 4))

""" 12)Написати функцію яка перетворює рядок на наступний формат. функція повинна ПОВЕРТАТИ рядок
            rebuild_string('test') = > tEsT
            rebuild_string('some string') = > sOmE sTrIng""
# task 12
def rebuild_string(input_string):
    result = ""


    for index in range(len(input_string)):

        if index % 2 == 0:

            result = result + input_string[index].lower()
        else:

            result = result + input_string[index].upper()

    return result

print(rebuild_string('test'))
print(rebuild_string('some string'))

""13)Написати функцію, яка змінює цифри на літери за принципом 0-А 1-B 2-C ... etc і ПОВЕРТАЄ строку proccess_str('231') => CDB ""
# task 13
def convert_digits_to_letters(input_string):
    result = ""

    alphabet_map = "ABCDEFGHIJ"

    for character in input_string:

        index = int(character)

        result = result + alphabet_map[index]

    return result

print(convert_digits_to_letters("231"))
print(convert_digits_to_letters("012"))
print(convert_digits_to_letters("987"))

""14)Написати функцію з розрахунку скільки витрачається грошей на кип'ятіння води в чайнику. На вхід подається початкова температура води та маса води. Функція повинна повернути кількість гривень.
            Q = C*m*(t2-t1), де:
            C - питома теплоємність, тобто. енергія, необхідна нагрівання в-ва на 1 градус. Для води за нормального тиску (101.325 кПа) це 4200 джоулів.
            m – маса, 1 літр води за звичайних умов має масу 1 кг.
            t2 – верхня температура нагріву, для нормального тиску температура кипіння води 100 градусів.
            t1 – початкова температура = кімнатна температура = у моєму випадку 25,6 гр.
        
            Q вимірюється у джоулях. 1Дж = 2.7778e-7 Кват/год. Необхідно перевести з Джуолей в кіловатий годинник.

             Вартість електроенергії можна взяти як 2,64 грн за 1кват/год."""
# task 14
def calculate_boiling_cost(initial_temperature, water_mass):
    SPECIFIC_HEAT_CAPACITY = 4200
    FINAL_TEMPERATURE = 100
    PRICE_PER_KWH = 2.64

    temperature_difference = FINAL_TEMPERATURE - initial_temperature

    energy_joules = SPECIFIC_HEAT_CAPACITY * water_mass * temperature_difference

    energy_in_kilowatt_hours = energy_joules * 2.7778e-7

    total_cost = energy_in_kilowatt_hours * PRICE_PER_KWH

    return round(total_cost, 4)


print(calculate_boiling_cost(25.6, 1))