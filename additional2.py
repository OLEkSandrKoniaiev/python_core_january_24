# 1)
# вивести послідовність Фібоначчі, кількість вказана в змінній,
#   наприклад: x = 10 -> 1 1 2 3 5 8 13 21 34 55
#   (число з послідовності - це сума попередніх двох чисел)
print('Завдання 1')


def fibonacci_sequence(amount: int = 2) -> list[int]:
    sequence: list[int] = [0, 1]  # почав з нуля
    for _ in range(amount - 2):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


print('()>', fibonacci_sequence())
print('(5)>', fibonacci_sequence(5))
print('(10)>', fibonacci_sequence(10))

# 2)
# порахувати кількість парних (even) і непарних (odd) цифр числа,
#   наприклад: х = 225688 -> п = 5, н = 1;
#          х = 33294 -> п = 2, н = 3
print('\nЗавдання 2')


def even_odd_counter(number: int) -> str:
    odds_count: int = 0
    evens_count: int = 0
    string: str = str(number)
    for char in string:
        if int(char) % 2 == 0:
            evens_count += 1
        else:
            odds_count += 1
    return f'п = {evens_count}, н = {odds_count}'


print('(120)> ', even_odd_counter(120))
print('(14305)> ', even_odd_counter(14305))

# 3)
# прога, що виводить кількість кожного символа з введеної строки,
# наприклад: st = 'as 23 fdfdg544'  # введена стрічка
# 'a' -> 1  # вивело в консолі
# 's' -> 1
# ' ' -> 2
# '2' -> 1
# '3' -> 1
# 'f' -> 2
# 'd' -> 2
# 'g' -> 1
# '5' -> 1
# '4' -> 2
print('\nЗавдання 3')


def each_character_amount(string: str) -> str:
    character_count: dict = dict()
    for char in string:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return '\n'.join(f"'{key}' -> {value}" for key, value in character_count.items())


print('input: (test)\n', each_character_amount('test'), sep='')
print('input: (as 23 fdfdg544)\n', each_character_amount('as 23 fdfdg544'), sep='')

# 4)
# генеруємо список із непарних чисел у порядку зростання [1,3,5,7,9.....n].
# завдання зробити з нього список списків такого плану:
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]  => [ [1], [3,5], [7,9,11], [13,15,17,19] ]
# [1, 3, 5, 7, 9, 11] => [[1], [3, 5], [7, 9, 11]]
# [1, 3, 5, 7, 9]  => [ [1], [3,5], [7,9]]
# [1, 3, 5, 7, 9, 11, 13]  => [[1], [3, 5], [7, 9, 11], [13]]
print('\nЗавдання 4')


def list_generator(number_list: list[int]) -> list[list[int]]:
    odd_list: list[int] = sorted([number for number in number_list if number % 2 == 1])
    output_list: list[list[int]] = []
    i, j = 0, 1

    while i < len(odd_list):

        temp_list: list[int] = []
        for _ in range(j):
            if i < len(number_list):
                temp_list.append(odd_list[i])
                i += 1

        # temp_list: list[int] = odd_list[i:i + j]
        # i += j

        j += 1
        output_list.append(temp_list)

    return output_list


print('([1, 2, 3, 4, 5])> ', list_generator([1, 2, 3, 4, 5]))
print('([1, 3, ... 103, 107])> ', list_generator([1, 3, 5, 7, 9, 11, 21, 23, 35, 57, 87, 101, 103, 107]))
print('([1, 21, ... 332, 4431])> ',
      list_generator([1, 21, 31, 127, 1370, 27, 8679, 23, 5, 0, 49, 43, 53, 3, 1, 56, 97, 332, 4431]))

# 5)
# знайти зі списку тільки унікальні числа
# приклад [1,2,3,4,2,5,1] => [ 3, 4, 5 ]
print('\nЗавдання 5')


def show_unique(number_list: list[int]) -> list[int]:
    unique_list: list[int] = []
    for number in number_list:  # трохи ресурсомісткий спосіб
        if number not in unique_list:
            unique_list.append(number)
        else:
            unique_list.remove(number)
    return unique_list


print('([1, 2, 3, 4, 3, 2])> ', show_unique([1, 2, 3, 4, 3, 2]))
