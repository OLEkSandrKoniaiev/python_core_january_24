# 1)
print('Strings - Завдання 1')


def extract_digits(string='example1'):
    digits = []
    for char in string:
        if char.isdigit():
            digits.append(char)
    print(','.join(digits))


extract_digits()
extract_digits('as 23 fdfdg544')
extract_digits('kjaskjasjio29u8ew8asgads8dqw891290eqpjj90 9 0QW9~^%&DSFS4')

# 2)
print('\nStrings - Завдання 2')


def extract_numbers(string='example1'):
    numbers = []
    number = ''
    prev_is_digit = False  # прапорець
    for char in string:
        if char.isdigit():
            number += char
            if not prev_is_digit:
                numbers.append(number)
                number = ''
        prev_is_digit = char.isdigit()
    print(', '.join(numbers))


extract_numbers()
extract_numbers('as 23 fdfdg544 34')
extract_numbers('kjaskjasjio29u8ew8asgads8dqw891290eqpjj90 9 0QW9~^%&DSFS4')

# 3)
print('\nList comprehension - Завдання 1')
greeting = 'Hello, world'

# print(list(greeting.upper()))

greeting_list = [char.upper() for char in greeting]
print(greeting_list)

# 4)
print('\nList comprehension - Завдання 2')
numbers_list = [number ** 2 for number in range(0, 50) if number % 2 == 1]
print(numbers_list)

# 5)
print('\nFunction - Завдання 1')


def print_list(my_list):
    str_list = [str(each) for each in my_list]
    # string = ', '.join(str_list)
    print('(print_list)>\t', ', '.join(str_list))


print_list([0, 1, 2, "Test", True, None])


def print_max(a=0, b=0, c=0):
    max_num = max(a, b, c)
    print('(print_max)>\t', max_num)
    return max_num


print_max(2, 3, 4)


def find_min_print_max(*args):
    print('(find_min_print_max)>\t', max(*args))
    return min(*args)


min_num = find_min_print_max(1, 2, 3, 4)
print('(find_min_print_max)>\t', min_num)


def find_max_from_list(my_list):
    num_list = [each for each in my_list if (type(each) is int or type(each) is float)]
    return max(num_list)


max_num_from_list = find_max_from_list([1, 2, 3, 4, True, 'Test'])
print('(find_max_from_list)>\t', max_num_from_list)


def find_min_from_list(my_list):
    num_list = [each for each in my_list if (type(each) is int or type(each) is float)]
    return min(num_list)


min_num_from_list = find_min_from_list([1, 2, 3, 4, True, 'Test'])
print('(find_min_from_list)>\t', min_num_from_list)


def number_from_list(num_list):
    output = ""
    for i in num_list:
        output += str(i)
    return int(output)


print('(number_from_list)>\t', number_from_list([1, 2, 3, 4]))


def average(my_list):
    return sum(my_list) / len(my_list)


print('(average)>\t', average([1, 2, 3, 4]))


# 6)
def find_min(my_list):
    min_number = my_list[0]
    for number in my_list:
        if number == 'X':
            continue
        if number < min_number:
            min_number = number
    print(min_number)


def delete_duplicates(my_list):
    my_set = set(my_list)
    my_list = list(my_set)
    print(my_list)


def every_4_is_x(my_list):
    for index, num in enumerate(my_list):
        if num == 'X':
            continue
        if index % 4 == 0 and index != 0:
            my_list[index] = 'X'
    print(my_list)


def print_square(size):
    if size < 2:
        print("Розмір повинен бути більше ніж два")
        return

    print('*' * size)

    for _ in range(size - 2):
        print('*' + ' ' * (size - 2) + '*')

    print('*' * size)


def multiplication_table():
    i = 1
    while i < 9:
        number_line = []
        j = 1
        while j <= 9:
            number_line.append(f"{i * j:2}")
            j += 1
        print(" ".join(number_line))
        i += 1


print('\nВітання в меню комплексного завдання!\nОберіть дію зі списком [22, 3,5,2,8,2,-23, 8,23,5]:')
print('1. Вивести мінімальне число\n'
      '2. Видалити усі дублікати\n'
      '3. Замінити кожне 4-те значення на \'X\'\n'
      '4. Вивести квадрат із зірочок\n'
      '5. Вивести таблицю множення\n'
      '6. Завершити програму')

is_going = True
our_list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
while is_going:
    user_choice = input('\n: ')

    if user_choice == '1':
        find_min(our_list)

    elif user_choice == '2':
        delete_duplicates(our_list)

    elif user_choice == '3':
        every_4_is_x(our_list)

    elif user_choice == '4':
        user_input = input('Розмір: ')
        print_square(int(user_input))

    elif user_choice == '5':
        multiplication_table()

    elif user_choice == '6':
        is_going = False
        print('Бажаю гарного дня!')

    else:
        print('Будь ласка введіть правильне число')
